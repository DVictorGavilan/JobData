import logging.config

from job_data import tecnoempleo
from datetime import date
from essentialkit import file_operations


logger = logging.getLogger(__name__)

def setup_logging():
    config_logging = file_operations.read_json("config/log_configuration.json")
    logging.config.dictConfig(config_logging)


def main():
    setup_logging()
    logger.info("Tecnoempleo ETL initialized")
    cutoff_date: date = date.today()
    tecnoempleo.pipeline.etl(cutoff_date=cutoff_date)
    logger.info("Tecnoempleo ETL completed")


if __name__ == "__main__":
    main()
