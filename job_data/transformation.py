import re
import pandas as pd


def add_date(value: str) -> str:
    value = value.strip()
    value = pd.to_datetime(value[:10], format='%d/%m/%Y')
    return value


def add_separete_description(value: str) -> str:
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', value)


def add_list_technologies(value: str) -> list:
    return []

def normalized_technologies(technologies: list) -> list:
    return []

