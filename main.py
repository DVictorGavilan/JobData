from datetime import date
from pandas import DataFrame
from job_data import scrapy, utils, pipeline


def main():
    cutoff_date: date = date.today()
    path_provincias_info: str = 'config/provincias_info.json'
    path_provincias_data: str = f'data/provincias_info_{cutoff_date}.csv'
    path_jobs_data: str       = f'data/empleos_info_{cutoff_date}.csv'

    provincias_info: dict = utils.read_json(path=path_provincias_info)

    provincias_data: DataFrame = scrapy.download_provincias_data(provincias_info)
    jobs_data: DataFrame       = scrapy.download_jobs_data(provincias_info)

    pipeline.processing_provincias_info(provincias_data).to_csv(path_provincias_data, index=False, sep=';')
    pipeline.processing_job_data(jobs_data).to_csv(path_jobs_data, index=False, sep=';')


if __name__ == '__main__':
    main()
