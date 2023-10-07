import re
import pandas as pd

from pandas import Timestamp

if __name__ == '__main__':
    print('sdf')

DATE_FORMAT = '%d/%m/%Y'
REGEX_SEPARATE_DESCRIPTION = r'(?<=[a-z])(?=[A-Z])', ' '
SEPARATE_TECHNOLOGIES = ' - '
REGEX_EXTRACT_AMOUNT = r'(\d+(\.\d{3})*\s*€\s*-\s*\d+(\.\d{3})*\s*€)'


def add_date(raw_value: str) -> Timestamp:
    raw_value = raw_value.strip()[:10]
    value = pd.to_datetime(arg=raw_value, format=DATE_FORMAT)
    return value


def add_separate_description(value: str) -> str:
    return re.sub(pattern=REGEX_SEPARATE_DESCRIPTION, string=value)


def add_list_technologies(value: str) -> list[str]:
    return value.split(SEPARATE_TECHNOLOGIES)


def extract_salary_amount(value: str) -> str | None:
    match = re.search(REGEX_EXTRACT_AMOUNT, value)
    if match:
        return match.group(1)
    else:
        return None


def normalized_technologies(technologies: list) -> list:
    return technologies
