import re
import pandas as pd
from typing import List
from typing import Optional

DATE_FORMAT = '%d/%m/%Y'
REGEX_SEPARETE_DESCPRIPTION = r'(?<=[a-z])(?=[A-Z])', ' '
SEPARATE_TECHNOLOGIES = ' - '
# Captura sueldos o rangos de sueldos en formato €, con o sin separador de miles (puntos).
# Ejemplos: "30.000€ - 42.000€", "30.000€"
REGEX_EXTRACT_AMOUNT = r'(\d+(\.\d{3})*\€(?:\s*-\s*\d+(\.\d{3})*\€)?)|(\d+(\.\d{3})*\€)'
# Expresión regular para encontrar las modalidades
REGEX_MODALIDAD =  re.compile(r'(presencial|hibrido|híbrido|remoto)', re.IGNORECASE)

def add_date(value: str) -> str:
    value = value.strip()
    value = pd.to_datetime(value[:10], format=DATE_FORMAT)
    return value


def add_separate_description(value: str) -> str:
    return re.sub(REGEX_SEPARETE_DESCPRIPTION, value)


def add_list_technologies(value: str) -> List[str]:
    return value.split(SEPARATE_TECHNOLOGIES)

# La descripción debe seguir el formato de sueldo único (ejm. 30.000€) o rango de sueldos (ejm., 30.000€ - 42.000€).
# Devuelve el sueldo o el rango de sueldos encontrado, o None si no se encontró ninguna información de sueldo.
def extract_salary_amount(descripcion: str) -> str:
    matches = re.findall(REGEX_EXTRACT_AMOUNT, descripcion)
    if matches:
        if matches[0][0]:
            return matches[0][0]
        elif matches[0][3]:
            return matches[0][3]
    return None

def extract_salary_min(salary: Optional[str]) -> Optional[float]:
    if salary is None:
        return None
    
    if '-' in salary:
        return float(salary.split(' - ')[0].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))

def extract_salary_max(salary: Optional[str]) -> Optional[float]:
    if salary is None:
        return None
    
    if '-' in salary:
        return float(salary.split(' - ')[1].replace('€', '').replace('.', ''))
    else:
        return float(salary.replace('€', '').replace('.', ''))
    
def extract_modalidad(descripcion: str) -> str:
    matches = REGEX_MODALIDAD.findall(descripcion)
    if matches:
        # Devolver la primera modalidad encontrada
        return matches[0].capitalize()  # Convertir la primera letra en mayúscula
    else:
        return None

def normalized_technologies(technologies: list) -> list:
    return []
