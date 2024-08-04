from job_data import tecnoempleo
from datetime import date


def main():

    cutoff_date: date = date.today()

    tecnoempleo.pipeline.etl(cutoff_date=cutoff_date)


if __name__ == "__main__":
    main()
