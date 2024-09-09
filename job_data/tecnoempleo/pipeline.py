import logging.config

from pandas import DataFrame
from datetime import date
from . import scraper, processing
from .quality import minimum_data_quality_expected


logger = logging.getLogger(__name__)


class PipelineException(Exception):
    """Custom exception for handling page not found errors."""
    pass


def extract() -> DataFrame:
    logger.info("Getting Tecnoempleo raw data")
    return DataFrame(data=scraper.download_job_data())


def transform(job_data_raw: DataFrame) -> DataFrame:
    logger.info("Getting Tecnoempleo master data")
    return processing.transformations(data=job_data_raw.copy())


def load(cutoff_date: date, job_data: DataFrame, zone: str) -> None:
    path_job_data = f"data/{zone}/tecnoempleo/data/job_data_{cutoff_date}.csv"
    logger.info(f"Saving data in {path_job_data}")
    job_data.to_csv(path_job_data, index=False, sep=",")


def etl(cutoff_date: date) -> None:
    job_data_raw: DataFrame = extract()
    job_data_master: DataFrame = transform(job_data_raw=job_data_raw)
    if minimum_data_quality_expected:
        logger.info(f"Minimum data quality exceeded")
        load(cutoff_date=cutoff_date, job_data=job_data_raw, zone="raw")
        load(cutoff_date=cutoff_date, job_data=job_data_master, zone="master")
    else:
        raise PipelineException("Minimum data quality failed")
