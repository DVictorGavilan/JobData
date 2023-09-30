import requests

from math import ceil
from pandas import DataFrame
from bs4 import BeautifulSoup
from requests import Response
from job_data import tecnoempleo
from bs4.element import Tag, ResultSet


def get_html(url: str) -> BeautifulSoup:
    response: Response = requests.get(url)
    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise 'Página no encontrada'


def generate_provincias_info_dict() -> dict[str: list[str]]:
    return {
        'id_provincia': [],
        'provincia': [],
        'num_ofertas': []
    }


def generate_jobs_info_dict() -> dict[str: list[str]]:
    return {
        'nombre_empleo': [],
        'empresa': [],
        'provincia': [],
        'tecnologias': [],
        'descripcion': [],
        'url': []
    }


def get_total_jobs(id: str) -> int:
    url: str = f"https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id},&pagina=1"
    soup: BeautifulSoup = get_html(url)
    header: str = soup.find(name=tecnoempleo.HEADER['tag'], attrs=tecnoempleo.HEADER['class_name']).text
    header_info: list[str] = [info.strip() for info in header.split(' ')]
    return int(header_info[0].replace('.', ''))


def download_provincias_data(info: dict) -> DataFrame:
    d_provincias_info: dict[str: list[str]] = generate_provincias_info_dict()
    for provincia in info['provincias']:
        n_total_jobs = get_total_jobs(provincia['id'])
        d_provincias_info['id_provincia'].append(provincia['id'])
        d_provincias_info['provincia'].append(provincia['name'])
        d_provincias_info['num_ofertas'].append(n_total_jobs)
    return DataFrame(d_provincias_info)


def download_jobs_data(info: dict) -> DataFrame:
    d_empleos_info = generate_jobs_info_dict()
    for provincia in info['provincias']:
        n_total_jobs = get_total_jobs(provincia['id'])
        pages = calculate_num_pages(n_total_jobs)
        for page in pages:
            url = f"https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{provincia['id']},&pagina={page}"
            soup: BeautifulSoup = get_html(url)
            divs_info: ResultSet[Tag] = soup.find_all(name=tecnoempleo.DIVS['tag'], attrs=tecnoempleo.DIVS['class_name'])
            for div in divs_info:
                job: str = div.find(name=tecnoempleo.JOB_NAME['tag'], attrs=tecnoempleo.JOB_NAME['class_name']).text.strip()
                job_url: str = div.find(name=tecnoempleo.JOB_URL['tag'], attrs=tecnoempleo.JOB_URL['class_name'])['href']
                company: str = div.find(name=tecnoempleo.COMPANY['tag'], attrs=tecnoempleo.COMPANY['class_name']).text.strip()
                technologies: str = ' - '.join([
                    technology.text.strip() for technology in div.find_all(name=tecnoempleo.TECHNOLOGIES['tag'], attrs=tecnoempleo.TECHNOLOGIES['class_name'])
                ])
                descripcion: str = ' '.join([
                    description.strip() for description in div.find(name=tecnoempleo.DESCRIPTION['tag'], attrs=tecnoempleo.DESCRIPTION['class_name']).text.split()
                ])
                d_empleos_info['nombre_empleo'].append(job)
                d_empleos_info['empresa'].append(company)
                d_empleos_info['provincia'].append(provincia['name'])
                d_empleos_info['tecnologias'].append(technologies)
                d_empleos_info['descripcion'].append(descripcion)
                d_empleos_info['url'].append(job_url)
    return DataFrame(d_empleos_info)


def calculate_num_pages(num: int) -> range:
    final_page: int = ceil(num / 30 + 1)
    return range(1, final_page)
