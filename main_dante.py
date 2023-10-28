import pandas as pd
from job_data import quality, transformation
from datetime import datetime

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

'''Comprobar si es tipo float'''
print('Validar los sueldos (float)')
print(quality.check_type(data_job, 'aux_salary_min',float))
print(quality.check_type(data_job, 'aux_salary_min',float))

# '''Extraer las modalidades de trabajo'''
# data_job['aux_modalidad'] = data_job['descripcion'].apply(transformation.extract_modality)
# print(data_job['aux_modalidad'].head(25))

# '''Check is empty'''
# print(data_job.apply(quality.df_is_empty))

print("Validación para 'aux_date':")
print(quality.check_type(data_job,'aux_date',datetime))