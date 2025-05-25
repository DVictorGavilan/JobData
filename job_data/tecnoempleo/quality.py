from pandas import DataFrame
from data_quality_kit import validity, completeness


def minimum_data_quality_expected(data: DataFrame) -> bool:
    """
    Data quality validations:
        - Dataframe is not empty.
        - There are not nulls on `job_url`.
        - There are not nulls on `job_name`.
        - There are not nulls on `job_company`.
        - There are not nulls on `cutoff_date`.
    :param data: Dataframe to validate.
    :return: True or False depending on validations output.
    """
    return all([
        completeness.assert_that_dataframe_is_empty(data),
        validity.assert_that_there_are_not_nulls(data, "job_url"),
        validity.assert_that_there_are_not_nulls(data, "job_name"),
        validity.assert_that_there_are_not_nulls(data, "job_company"),
        validity.assert_that_there_are_not_nulls(data, "cutoff_date")
    ])
