from datetime import date
import pandas as pd
import requests

from math import ceil
from bs4 import BeautifulSoup
from pandas import DataFrame
from requests import Response
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


def get_provincias_info() -> dict[str: list[str]]:
    d_provincias_info: dict[str: list[str]] = gen_d_provincias_info()
    for id_provincia in range(231, 231 + 52):
        url: str = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina=1'
        soup: BeautifulSoup = get_html(url)
        header: str = soup.find('h1', class_='h5 h6-xs').text
        header_info: list[str] = [info.strip() for info in header.split(' ')]
        d_provincias_info['id_provincia'].append(id_provincia)
        d_provincias_info['provincia'].append(' '.join(header_info[6:]))
        d_provincias_info['num_ofertas'].append(
            header_info[0].replace('.', ''))
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


def gen_empleos_info(df: DataFrame):
    d_empleos_info: dict[str: list[str]] = gen_d_empleos_info()
    for id_provincia in range(231, 231 + 52):
        provincia_num: bool = df_provincias_info['id_provincia'] == id_provincia
        num_pages: float = df_provincias_info[provincia_num]['num_ofertas'].values[0]
        for page in gen_num_pages(num_pages):
            url = f'https://www.tecnoempleo.com/busqueda-empleo.php?pr=,{id_provincia},&pagina={page}'
            soup: BeautifulSoup = get_html(url)
            divs_info: ResultSet[Tag] = soup.find_all(
                'div', class_='p-2 border-bottom py-3 bg-white')
            for div in divs_info:
                empleo: str = div.find(
                    'h3', class_='h5 h6-xs mb-2').text.strip()
                empleo_url: str = div.find(
                    'a', class_='font-weight-bold text-gray-700')['href']
                empresa: str = div.find(
                    'a', class_='text-primary').text.strip()
                provincia: str = df_provincias_info[provincia_num]['provincia'].values[0]
                lenguajes: str = ' - '.join([leng.text.strip() for leng in div.find_all('a',
                                                                                        class_='badge bg-primary-soft bg-primary-hover fw-normal font-weight-normal fs--14 mr-2 me-2')])
                descripcion: str = ' '.join([desc.strip() for desc in div.find('div',
                                                                               class_='col-12 col-lg-3 text-gray-600 pt-2 line-height-10 text-right hidden-md-down').text.split()])
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

def verificar_nulos_en_columna(df: pd.DataFrame, columna: str) -> bool:
    if columna not in df.columns:
        raise ValueError(f'La columna "{columna}" no existe en el DataFrame.')

    return df[columna].isnull().any()

# print(verificar_nulos_en_columna(df,'nombre_empleo'))
# print(verificar_nulos_en_columna(df,'empresa'))
# print(verificar_nulos_en_columna(df,'provincia'))
# print(verificar_nulos_en_columna(df,'tecnologias'))
# print(verificar_nulos_en_columna(df,'descripcion'))
# print(verificar_nulos_en_columna(df,'url'))

df_provincias_info: DataFrame = DataFrame(get_provincias_info())
path_provincias_info: str = f'data/provincias_info_{date.today()}.csv'
df_provincias_info.to_csv(path_provincias_info, index=False, sep=';')

df_provincias_info: DataFrame = pd.read_csv(
    path_provincias_info, header=[0], sep=';')

df_empleos_info: DataFrame = DataFrame(gen_empleos_info(df_provincias_info))
path_provincias_info: str = f'data/empleos_info_{date.today()}.csv'
df_empleos_info.to_csv(path_provincias_info, index=False, sep=';')

