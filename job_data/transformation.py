import re
import pandas as pd
from typing import List


DATE_FORMAT = '%d/%m/%Y'
REGEX_SEPARETE_DESCPRIPTION = r'(?<=[a-z])(?=[A-Z])', ' '
SEPARATE_TECHNOLOGIES = ' - '
REGEX_EXTRACT_AMOUNT = r'(\d+(\.\d{3})*\s*€\s*-\s*\d+(\.\d{3})*\s*€)'

def add_date(value: str) -> str:
    value = value.strip()
    value = pd.to_datetime(value[:10], format=DATE_FORMAT)
    return value


def add_separate_description(value: str) -> str:
    return re.sub(REGEX_SEPARETE_DESCPRIPTION, value)


def add_list_technologies(value: str) -> List[str]:
    return value.split(SEPARATE_TECHNOLOGIES)

def extract_salary_amount(value: str) -> str:
    match = re.search(REGEX_EXTRACT_AMOUNT, value)
    if match:
        return match.group(1)
    else:
        return None

def normalized_technologies(technologies: list) -> list:
    return []
