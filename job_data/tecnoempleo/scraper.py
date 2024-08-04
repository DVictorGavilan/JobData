import requests

from bs4 import BeautifulSoup, Tag, ResultSet
from requests import Response
from job_data.tecnoempleo import catalog_tag, utils


class ElementNotFound(Exception):
    """Custom exception for handling page not found errors."""
    pass


def get_html(url: str) -> BeautifulSoup:
    try:
        response: Response = requests.get(url=url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(markup=response.content, features="html.parser")
    except requests.exceptions.RequestException:
        raise


def get_total_jobs(soup: BeautifulSoup) -> int:
    header_tag = catalog_tag.HEADER
    header: Tag = soup.find(name=header_tag["name"], attrs=header_tag["class"])
    if header:
        total_jobs = header.text.replace('.', '') .split(' ')[0]
        return int(total_jobs)
    raise ElementNotFound(f"{header_tag}")


def get_job_divs(soup: BeautifulSoup) -> ResultSet[Tag]:
    job_divs_tag: dict = catalog_tag.DIVS
    element: ResultSet[Tag] = soup.find_all(name=job_divs_tag["name"], attrs=job_divs_tag["class"])
    if element:
        return element
    raise ElementNotFound(f"{job_divs_tag}")


def get_job_name(job_div: Tag) -> str:
    job_name_tag: dict = catalog_tag.JOB_NAME
    element: Tag = job_div.find(name=job_name_tag["name"], attrs=job_name_tag["class"])
    if element:
        return element.attrs.get("title")
    raise ElementNotFound(f"{job_name_tag}")


def get_job_url(job_div: Tag) -> str:
    job_url_tag: dict = catalog_tag.JOB_URL
    element: Tag = job_div.find(name=job_url_tag["name"], attrs=job_url_tag["class"])
    if element:
        return element["href"]
    raise ElementNotFound(f"{job_url_tag}")


def get_job_company(job_div: Tag) -> str:
    job_company_tag: dict = catalog_tag.JOB_COMPANY
    element: Tag = job_div.find(name=job_company_tag["name"], attrs=job_company_tag["class"])
    if element:
        return element.text.strip()
    raise ElementNotFound(f"{job_company_tag}")


def get_job_technologies_stack(job_div: Tag) -> list[str]:
    job_technologies_stack_tag: dict = catalog_tag.JOB_TECHNOLOGIES_STACK
    elements: ResultSet[Tag] = job_div.find_all(name=job_technologies_stack_tag["name"], attrs=job_technologies_stack_tag["class"])
    if elements:
        return [technology.text.strip() for technology in elements]
    raise ElementNotFound(f"{job_technologies_stack_tag}")


def get_job_description(job_div: Tag) -> str:
    job_description_tag: dict = catalog_tag.JOB_DESCRIPTION
    element: Tag = job_div.find(name=job_description_tag["name"], attrs=job_description_tag["class"])
    if element:
        return utils.get_iterator_element_by_index(element.children, 2)
    raise ElementNotFound(f"{job_description_tag}")


def get_job_other_info(job_div: Tag) -> str:
    job_description_tag: dict = catalog_tag.JOB_OTHER_DATA
    element: Tag = job_div.find(name=job_description_tag["name"], attrs=job_description_tag["class"])
    if element:
        return element.text.strip()
    raise ElementNotFound(f"{job_description_tag}")


def extract_job_data(job_div: Tag) -> dict:
    print(get_job_url(job_div))
    return {
        "job_url": get_job_url(job_div),
        "job_name": get_job_name(job_div),
        "job_company": get_job_company(job_div),
        "job_technologies_stack": get_job_technologies_stack(job_div),
        "job_description": get_job_description(job_div),
        "job_other_info": get_job_other_info(job_div),
    }


# def generate_city_data(city_id: str, city_name: str) -> dict:
#     url: str = utils.generate_url(city_id=city_id)
#     soup: BeautifulSoup = get_html(url=url)
#     total_jobs: int = get_total_jobs(soup=soup)
#     total_pages: range = utils.calculate_total_pages_num(total_jobs=total_jobs)
#     return {
#         "id": city_id,
#         "name": city_name,
#         "total_num_of_jobs": total_jobs,
#         "total_num_of_pages": total_pages
#     }


# def download_cities_data(cities_info: list[dict]) -> list[dict]:
#     cities_data = []
#     for city in cities_info:
#         city_data = generate_city_data(city_id=city["id"], city_name=city["name"])
#         cities_data.append(city_data)
#     return cities_data


# def download_job_data_(cities_info: list[dict]) -> list[dict]:
#     job_data = []
#     for city in cities_info:
#         for page in city["total_num_of_pages"]:
#             url: str = utils.generate_url(city_id=city["id"], page=page)
#             html: BeautifulSoup = get_html(url=url)
#             divs_info: ResultSet[Tag] = get_job_divs(soup=html)
#             for div in divs_info:
#                 data_in_div = extract_job_data(job_div=div)
#                 data_in_div.update({'job_city': city["name"]})
#                 job_data.append(data_in_div)
#     return job_data


def download_job_data() -> list[dict]:
    job_data = []
    url: str = utils.generate_base_url()
    soup: BeautifulSoup = get_html(url=url)
    total_jobs: int = get_total_jobs(soup=soup)
    total_pages: range = utils.calculate_total_pages_num(total_jobs=total_jobs)
    for page in total_pages:
        url_page = utils.generate_base_url(page=page)
        html: BeautifulSoup = get_html(url=url_page)
        divs_info: ResultSet[Tag] = get_job_divs(soup=html)
        for div in divs_info:
            data_in_div = extract_job_data(job_div=div)
            job_data.append(data_in_div)
    return job_data
