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


def gen_d_provincias_info() -> dict[str: list[str]]:
    d_provincias_info = {
        'id_provincia': [],
        'provincia': [],
        'num_ofertas': []
    }
    return d_provincias_info



def get_total_jobs(id: str) -> int:
    url: str = f"https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id},&pagina=1"
    soup: BeautifulSoup = get_html(url)
    header: str = soup.find(name=tecnoempleo.HEADER['tag'], attrs=tecnoempleo.HEADER['class_name']).text
    header_info: list[str] = [info.strip() for info in header.split(' ')]
    return int(header_info[0].replace('.', ''))


def get_provincias_info(info: dict) -> dict[str: list[str]]:
    d_provincias_info: dict[str: list[str]] = gen_d_provincias_info()
    for provincia in info['provincias']:
        n_total_jobs = get_total_jobs(provincia['id'])
        d_provincias_info['id_provincia'].append(provincia['id'])
        d_provincias_info['provincia'].append(provincia['name'])
        d_provincias_info['num_ofertas'].append(n_total_jobs)
    return d_provincias_info


def gen_d_empleos_info() -> dict[str: list[str]]:
    dic_empleos_info: dict[str: list[str]] = {
        'nombre_empleo': [],
        'empresa': [],
        'provincia': [],
        'tecnologias': [],
        'descripcion': [],
        'url': []
    }
    return dic_empleos_info


def gen_empleos_info(df: DataFrame) -> dict[str: list[str]]:
    d_empleos_info = gen_d_empleos_info()
    for id_provincia in range(231, 231 + 52):
        provincia_num = df['id_provincia'] == id_provincia
        num_pages = df[provincia_num]['num_ofertas'].values[0]
        for page in gen_num_pages(num_pages):
            url = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina={page}'
            soup: BeautifulSoup = get_html(url)
            divs_info: ResultSet[Tag] = soup.find_all(name=tecnoempleo.DIVS['tag'], attrs=tecnoempleo.DIVS['class_name'])
            for div in divs_info:
                empleo: str = div.find(name=tecnoempleo.EMPLEO_NAME['tag'], attrs=tecnoempleo.EMPLEO_NAME['class_name']).text.strip()
                empleo_url: str = div.find(name=tecnoempleo.EMPLEO_URL['tag'], attrs=tecnoempleo.EMPLEO_URL['class_name'])['href']
                empresa: str = div.find(name='a', attrs={'class': 'text-primary'}).text.strip()
                provincia: str = df[provincia_num]['provincia'].values[0]
                lenguajes: str = ' - '.join([leng.text.strip() for leng in div.find_all(name=tecnoempleo.LENGUAJES['tag'], attrs=tecnoempleo.LENGUAJES['class_name'])])
                descripcion: str = ' '.join([desc.strip() for desc in div.find(name=tecnoempleo.DESCRIPCION['tag'], attrs=tecnoempleo.DESCRIPCION['class_name']).text.split()])
                d_empleos_info['nombre_empleo'].append(empleo)
                d_empleos_info['empresa'].append(empresa)
                d_empleos_info['provincia'].append(provincia)
                d_empleos_info['tecnologias'].append(lenguajes)
                d_empleos_info['descripcion'].append(descripcion)
                d_empleos_info['url'].append(empleo_url)
    return d_empleos_info


def gen_num_pages(num: int) -> range:
    final_page: int = ceil(num / 30 + 1)
    return range(1, final_page)
