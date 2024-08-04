from pandas import DataFrame
from data_quality_kit import validate_nulls


def quality(data: DataFrame) -> None:
    validate_nulls.check_nulls(data, "job_url")
    validate_nulls.check_nulls(data, "job_name")
    validate_nulls.check_nulls(data, "job_company")
    validate_nulls.check_nulls(data, "job_city")
