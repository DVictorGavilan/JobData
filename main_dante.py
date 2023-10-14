import pandas as pd
from job_data import quality, transformation

def count_repeated_values(elements: list) -> dict:
    return {element: elements.count(element) for element in set(elements)}

data_job = pd.read_csv('data/empleos_info_2023-09-30.csv', sep=';')

data_job['descripcion'] = data_job['descripcion'].str.lower()

data_job['aux_date']        = data_job['descripcion'].apply(transformation.add_date)
print(data_job['aux_date'].head(15))

'''Extraer los sueldos'''
data_job['aux_salary'] = data_job['descripcion'].apply(transformation.extract_salary_amount)
print(data_job['aux_salary'].head(10))

'''Crear las nuevas columnas con las funciones aplicadas'''
data_job['aux_salary_min'] = data_job['aux_salary'].apply(transformation.extract_salary_min)
data_job['aux_salary_max'] = data_job['aux_salary'].apply(transformation.extract_salary_max)
print(data_job[['aux_salary', 'aux_salary_min', 'aux_salary_max']].head(10))

'''Extraer las modalidades de trabajo'''
data_job['aux_modalidad'] = data_job['descripcion'].apply(transformation.extract_modality)
print(data_job['aux_modalidad'].head(25))