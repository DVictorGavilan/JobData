import re
import pandas as pd
from typing import List

def add_date(value: str) -> str:
    value = value.strip()
    value = pd.to_datetime(value[:10], format='%d/%m/%Y')
    return value


def add_separete_description(value: str) -> str:
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', value)


def add_list_technologies(value: str) -> List[str]:
    # Dividir la cadena en una lista usando ' - ' como separador
    tech_list = value.split(' - ')
    return tech_list

def normalized_technologies(technologies: list) -> list:
    return []

