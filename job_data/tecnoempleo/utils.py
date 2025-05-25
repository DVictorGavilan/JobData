from math import ceil
from itertools import islice


def calculate_total_pages_num(total_jobs: int) -> range:
    """
    Calculate the total number of pages needed to display all jobs.

    Given the total number of jobs, this function determines the number of
    pages required if each page can display up to 30 jobs. The function returns
    a range object representing the sequence of page numbers.

    :param total_jobs: The total number of jobs that need to be displayed
    :return: A range object starting from 1 to the calculated total number of
        pages. The end of the range is non-inclusive
    """
    last_num_page: int = ceil(total_jobs / 30 + 1)
    return range(1, last_num_page)


def generate_base_url(page: int = 1) -> str:
    """
    Generate the URL for a specific page of job listings on Tecnoempleo.

    This function constructs the URL for the Tecnoempleo job listings page,
    including the specified page number as a query parameter. The default page
    number is 1.

    :param page: The page number to be included in the URL query parameter.
        Defaults to 1.
    :return: The formatted URL string for the specified page of job listings.
    """
    return f"https://www.tecnoempleo.com/ofertas-trabajo/?pagina={page}"


def generate_url_for_city_and_page(city_id: str, page: int = 1):
    """
    Generate the URL for a specific city and page of job listings on
    Tecnoempleo.

    This function constructs the URL for the Tecnoempleo job listings page,
    including the specified city and page number as a query parameter. The
    default page number is 1.

    :param city_id: The city code to be included in the URL query parameter.
    :param page: The page number to be included in the URL query parameter.
        Defaults to 1.
    :return: The formatted URL string for the specified city and page of
        job listings.
    """
    return f"https://www.tecnoempleo.com/busqueda-empleo.php?pr={city_id}&pagina={page}"


def get_iterator_element_by_index(iterator, index):
    """
    Retrieve an element from an iterator by its index.

    This function uses `islice` to advance the iterator to the desired index
    and returns the element at that position. If the index is out of range,
    the function returns `None`.
    :param iterator: The iterator from which to retrieve the element.
    :param index: The zero-based index of the element to retrieve.
    :return: The element at the specified index, or `None` if the index is
        out of range.
    """
    return next(islice(iterator, index, index + 1), None)
