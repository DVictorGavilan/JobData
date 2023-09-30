import pandas as pd

from datetime import date
from pandas import DataFrame
from job_data import scrapy, utils


path_provincias_info = 'config/provincias_info.json'
provincias_info = utils.read_json(path=path_provincias_info)

df_provincias_info: DataFrame = DataFrame(scrapy.get_provincias_info(provincias_info))
# path_provincias_info: str = f'data/provincias_info_{date.today()}.csv'
# df_provincias_info.to_csv(path_provincias_info, index=False, sep=';')

# df_provincias_info: DataFrame = pd.read_csv(path_provincias_info, header=[0], sep=';')

# df_empleos_info: DataFrame = DataFrame(scrapy.gen_empleos_info(df_provincias_info))
# path_provincias_info: str = f'data/empleos_info_{date.today()}.csv'
# df_empleos_info.to_csv(path_provincias_info, index=False, sep=';')


