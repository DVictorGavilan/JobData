from datetime import date
from math import ceil

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, ResultSet
from pandas import DataFrame
from requests import Response


def get_html(url: str) -> BeautifulSoup:
    response: Response = requests.get(url)
    if response.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise 'Página no encontrada'


def gen_d_provincias_info() -> dict[str: list[str]]:
    d_provincias_info: dict[str: list[str]] = {
        'id_provincia': list(),
        'provincia': list(),
        'num_ofertas': list()
    }
    return d_provincias_info


def get_provincias_info() -> dict[str: list[str]]:
    d_provincias_info: dict[str: list[str]] = gen_d_provincias_info()
    for id_provincia in range(231, 231 + 52):
        url: str = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina=1'
        soup: BeautifulSoup = get_html(url)
        header: str = soup.find('h1', class_='h5 h6-xs').text
        header_info: list[str] = [info.strip() for info in header.split(' ')]
        d_provincias_info['id_provincia'].append(id_provincia)
        d_provincias_info['provincia'].append(' '.join(header_info[6:-4]))
        d_provincias_info['num_ofertas'].append(header_info[0].replace('.', ''))
    return d_provincias_info


def gen_d_empleos_info() -> dict[str: list[str]]:
    dic_empleos_info: dict[str: list[str]] = {
        'nombre_empleo': list(),
        'empresa': list(),
        'provincia': list(),
        'tecnologias': list(),
        'descripcion': list(),
        'url': list()
    }
    return dic_empleos_info


def gen_empleos_info(df: DataFrame):
    d_empleos_info: dict[str: list[str]] = gen_d_empleos_info()
    for id_provincia in range(231, 231 + 52):
        provincia_num: bool = df_provincias_info['id_provincia'] == id_provincia
        num_pages: float = df_provincias_info[provincia_num]['num_ofertas'].values[0]
        for page in gen_num_pages(num_pages):
            url = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina={page}'
            soup: BeautifulSoup = get_html(url)
            divs_info: ResultSet[Tag] = soup.find_all('div', class_='p-2 border-bottom py-3 bg-white')
            for div in divs_info:
                empleo: str = div.find('h3', class_='h5 h6-xs mb-2').text.strip()
                empleo_url: str = div.find('a', class_='font-weight-bold text-gray-700 link-muted')['href']
                empresa: str = div.find('a', class_='text-primary').text.strip()
                provincia: str = df_provincias_info[provincia_num]['provincia'].values[0]
                lenguajes: str = ' - '.join([leng.text.strip() for leng in div.find_all('a',
                                                                                        class_='badge-pill badge-soft badge-primary text-primary text-warning-hover py-1 px-2 fs--13 mr-1')])
                descripcion: str = ' '.join([desc.strip() for desc in div.find('div',
                                                                               'col-12 col-lg-3 text-gray-600 pt-2 line-height-10 text-right hidden-md-down').text.split()])
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


df_provincias_info: DataFrame = DataFrame(get_provincias_info())
path_provincias_info: str = f'data/provincias_info_{date.today()}.csv'
df_provincias_info.to_csv(path_provincias_info, index=False, sep=';')

df_provincias_info: DataFrame = pd.read_csv(path_provincias_info, header=[0], sep=';')

df_empleos_info: DataFrame = DataFrame(gen_empleos_info(df_provincias_info))
path_provincias_info: str = f'data/empleos_info_{date.today()}.csv'
df_empleos_info.to_csv(path_provincias_info, index=False, sep=';')
