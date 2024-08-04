from math import ceil
from itertools import islice


def calculate_total_pages_num(total_jobs: int) -> range:
    last_num_page: int = ceil(total_jobs / 30 + 1)
    return range(1, last_num_page)


def generate_url(city_id: str, page: int = 1):
    return f"https://www.tecnoempleo.com/busqueda-empleo.php?pr={city_id}&pagina={page}"


def generate_base_url(page: int = 1) -> str:
    return f"https://www.tecnoempleo.com/ofertas-trabajo/?pagina={page}"


def get_iterator_element_by_index(iterator, index):
    return next(islice(iterator, index, index + 1), None)


if __name__ == '__main__':
    ...
