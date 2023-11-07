import re
import pandas as pd
from pandas import Series

DATE_FORMAT = '%d/%m/%Y'
SEPARATE_TECHNOLOGIES = ' - '
REGEX_EXTRACT_AMOUNT = r'(\d+(\.\d{3})*\€(?:\s*-\s*\d+(\.\d{3})*\€)?)|(\d+(\.\d{3})*\€)'
REGEX_MODALIDAD = r'(presencial|hibrido|híbrido|remoto)'


def add_date(value: Series) -> Series:
    value = value.strip()
    value = pd.to_datetime(value[:10], format=DATE_FORMAT)
    return value


def add_list_technologies(value: str) -> list[str]:
    return value.split(SEPARATE_TECHNOLOGIES)


def extract_salary_amount(descripcion: str) -> str | None:
    matches = re.findall(REGEX_EXTRACT_AMOUNT, descripcion)
    if matches:
        if matches[0][0]:
            return matches[0][0]
        elif matches[0][3]:
            return matches[0][3]
    return None


def extract_salary_min(salary: str) -> float | None:
    if salary is None:
        return None
    if '-' in salary:
        return float(salary.split(' - ')[0].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))


def extract_salary_max(salary: str) -> float | None:
    if salary is None:
        return None
    if '-' in salary:
        return float(salary.split(' - ')[1].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))


def extract_modality(description: str) -> str | None:
    matches = re.findall(REGEX_MODALIDAD, description)
    if matches:
        return matches[0].capitalize()
    else:
        return None


# def normalized_technology_name(raw_name: str, normal: dict) -> str:
#     if raw_name in normal.keys():
#         return normal[raw_name]
#     else:
#         return raw_name
#
#
# def normalized_technologies(technologies: list, normalized_names: dict) -> list:
#     return [normalized_technology_name(technology, normalized_names) for technology in technologies]
