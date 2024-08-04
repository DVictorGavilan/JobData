from . import scraper, processing

from datetime import date
from pandas import DataFrame


def extract() -> DataFrame:
    return DataFrame(scraper.download_job_data())


def transform(job_data_raw: DataFrame) -> DataFrame:
    return processing.transformations(data=job_data_raw)


def load(cutoff_date: date, job_data: DataFrame, zone: str) -> None:
    path_job_data = f"data/{zone}/tecnoempleo/job_data_{cutoff_date}.csv"
    job_data.to_csv(path_job_data, index=False, sep=";")


def etl(cutoff_date: date):
    job_data_raw: DataFrame = extract()
    job_data_master: DataFrame = transform(job_data_raw=job_data_raw)
    load(cutoff_date=cutoff_date, job_data=job_data_raw, zone="raw")
    load(cutoff_date=cutoff_date, job_data=job_data_master, zone="master")
