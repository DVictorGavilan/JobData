import re
import pandas as pd
from pandas import Series
from typing import List

DATE_FORMAT = '%d/%m/%Y'
SEPARATE_TECHNOLOGIES = ' - '
REGEX_EXTRACT_AMOUNT = r'(\d+(\.\d{3})*\€(?:\s*-\s*\d+(\.\d{3})*\€)?)|(\d+(\.\d{3})*\€)'
REGEX_MODALIDAD = r'(presencial|hibrido|híbrido|remoto)'

def add_date(value: Series) -> Series:
    value = value.strip()
    value = pd.to_datetime(value[:10], format=DATE_FORMAT)
    return value

def add_list_technologies(value: str) -> List[str]:
    return value.split(SEPARATE_TECHNOLOGIES)

def extract_salary_amount(descripcion: str) -> str:
    matches = re.findall(REGEX_EXTRACT_AMOUNT, descripcion)
    if matches:
        if matches[0][0]:
            return matches[0][0]
        elif matches[0][3]:
            return matches[0][3]
    return None

def extract_salary_min(salary: str) -> float:
    if salary is None:
        return None

    if '-' in salary:
        return float(salary.split(' - ')[0].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))

def extract_salary_max(salary: str) -> float:
    if salary is None:
        return None

    if '-' in salary:
        return float(salary.split(' - ')[1].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))

def extract_modality(descripcion: str) -> str:
    matches = re.findall(REGEX_MODALIDAD, descripcion)
    if matches:
        return matches[0].capitalize()
    else:
        return None

def normalized_technologies(technologies: list) -> list:
    return []
