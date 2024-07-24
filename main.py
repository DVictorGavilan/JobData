from datetime import date
from pandas import DataFrame
from essentialkit import file_operations
from job_data.tecnoempleo import scraper


def main():
    cutoff_date: date = date.today()
    path_cities_info = 'config/tecnoempleo/cities_info.json'
    path_cities_data = f'data/raw/cities_data_{cutoff_date}.csv'
    path_job_data = f'data/raw/job_data_{cutoff_date}.csv'

    cities_info = file_operations.read_json(path=path_cities_info)

    city = scraper.download_cities_data(cities_info)
    cities_data: DataFrame = DataFrame(city)
    job_data: DataFrame = DataFrame(scraper.download_job_data(city))

    cities_data.to_csv(path_cities_data, index=False, sep=";")
    job_data.to_csv(path_job_data, index=False, sep=";")

    # pipeline.processing_cities_info(cities_data).to_csv(path_cities_data, index=False, sep=';')
    # pipeline.processing_job_data(job_data).to_csv(path_jobs_data, index=False, sep=';')


if __name__ == '__main__':
    main()
