import pandas as pd

from datetime import date
from pandas import DataFrame
from job_data import scrapy, quality, transformation, utils


path_provincias_info = 'config/provincias_info.json'
provincias_info = utils.read_json(path=path_provincias_info)

# df_provincias_info: DataFrame = DataFrame(scrapy.get_provincias_info(provincias_info))
# path_provincias_info: str = f'data/provincias_info_{date.today()}.csv'
# df_provincias_info.to_csv(path_provincias_info, index=False, sep=';')

# df_provincias_info: DataFrame = pd.read_csv(path_provincias_info, header=[0], sep=';')

# df_empleos_info: DataFrame = DataFrame(scrapy.gen_empleos_info(df_provincias_info))
# path_provincias_info: str = f'data/empleos_info_{date.today()}.csv'
# df_empleos_info.to_csv(path_provincias_info, index=False, sep=';')

for provincia in provincias_info['provincias']:
    print(provincia['name'], scrapy.get_total_jobs(provincia['id']))
    break

##############################################################################################

# for column in df_empleos_info.columns:
    # quality.check_nulls(df_empleos_info, columna=column)

##############################################################################################

# data_job = pd.read_csv('data/empleos_info_2023-09-24.csv', sep=';')
# data_job['aux_date']        = data_job['descripcion'].apply(transformation.add_date)
# data_job['aux_descripcion'] = data_job['descripcion'].apply(transformation.add_separete_description)
