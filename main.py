import json
import requests
import pandas as pd

from math import ceil
from bs4 import BeautifulSoup
from pandas import DataFrame
from datetime import date
from requests import Response
from bs4.element import Tag, ResultSet


HEADER = {
    'tag': 'h1',
    'class_name': {'class': 'h5 h6-xs'}
}

DIVS = {
    'tag': 'div',
    'class_name': {'class': 'p-2 border-bottom py-3 bg-white'}
}

EMPLEO_NAME = {
    'tag': 'h3',
    'class_name': {'class': 'h5 h6-xs mb-2'}
}

EMPLEO_URL = {
    'tag': 'a',
    'class_name': {'class': 'font-weight-bold text-gray-700'}
}

EMPRESA = {
    'tag': 'a',
    'class_name': {'class': 'text-primary'}
}

LENGUAJES = {
    'tag': 'a',
    'class_name': {'class': 'badge bg-primary-soft bg-primary-hover fw-normal font-weight-normal fs--14 mr-2 me-2'}
}

DESCRIPCION = {
    'tag': 'div',
    'class_name': {'class': 'col-12 col-lg-3 text-gray-600 pt-2 line-height-10 text-right hidden-md-down'}
}

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


def get_provincias_info(info: dict) -> dict[str: list[str]]:
    d_provincias_info: dict[str: list[str]] = gen_d_provincias_info()
    for provincia in info['provincias']:
        url: str = f"https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{provincia['id']},&pagina=1"
        soup: BeautifulSoup = get_html(url)
        header: str = soup.find(name=HEADER['tag'], attrs=HEADER['class_name']).text
        header_info: list[str] = [info.strip() for info in header.split(' ')]
        d_provincias_info['id_provincia'].append(provincia['id'])
        d_provincias_info['provincia'].append(' '.join(header_info[6:]))
        d_provincias_info['num_ofertas'].append(header_info[0].replace('.', ''))
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


def gen_empleos_info(df_provincias_info: DataFrame) -> dict[str: list[str]]:
    d_empleos_info: dict[str: list[str]] = gen_d_empleos_info()
    for id_provincia in range(231, 231 + 52):
        provincia_num: bool = df_provincias_info['id_provincia'] == id_provincia
        num_pages: float = df_provincias_info[provincia_num]['num_ofertas'].values[0]
        for page in gen_num_pages(num_pages):
            url = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina={page}'
            soup: BeautifulSoup = get_html(url)
            divs_info: ResultSet[Tag] = soup.find_all(name=DIVS['tag'], attrs=DIVS['class_name'])
            for div in divs_info:
                empleo: str = div.find(name=EMPLEO_NAME['tag'], attrs=EMPLEO_NAME['class_name']).text.strip()
                empleo_url: str = div.find(name=EMPLEO_URL['tag'], attrs=EMPLEO_URL['class_name'])['href']
                empresa: str = div.find(name='a', attrs={'class': 'text-primary'}).text.strip()
                provincia: str = df_provincias_info[provincia_num]['provincia'].values[0]
                lenguajes: str = ' - '.join([leng.text.strip() for leng in div.find_all(name=LENGUAJES['tag'], attrs=LENGUAJES['class_name'])])
                descripcion: str = ' '.join([desc.strip() for desc in div.find(name=DESCRIPCION['tag'], attrs=DESCRIPCION['class_name']).text.split()])
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


provincias_info_path = 'data/provincia_info.json'

with open(file=provincias_info_path, mode='r', encoding='utf-8') as f:
  provincias_info = json.load(f)

df_provincias_info: DataFrame = DataFrame(get_provincias_info(provincias_info))
path_provincias_info: str = f'data/provincias_info_{date.today()}.csv'
df_provincias_info.to_csv(path_provincias_info, index=False, sep=';')

df_provincias_info: DataFrame = pd.read_csv(path_provincias_info, header=[0], sep=';')

df_empleos_info: DataFrame = DataFrame(gen_empleos_info(df_provincias_info))
path_provincias_info: str = f'data/empleos_info_{date.today()}.csv'
df_empleos_info.to_csv(path_provincias_info, index=False, sep=';')
