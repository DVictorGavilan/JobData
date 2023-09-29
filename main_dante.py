import pandas as pd

from job_data import quality, transformation


data_job = pd.read_csv('data/empleos_info_2023-09-24.csv', sep=';')

for column in data_job.columns:
    quality.check_nulls(data_job, columna=column)

data_job['aux_date']        = data_job['descripcion'].apply(transformation.add_date)
data_job['aux_descripcion'] = data_job['descripcion'].apply(transformation.add_separete_description)

print(data_job[['aux_date', 'aux_descripcion']].head().to_string())
