import pandas
import logging.config

from pandas import DataFrame
from datetime import datetime
from job_data.tecnoempleo import constants


logger = logging.getLogger(__name__)


def normalized_job_description_column(data: DataFrame) -> DataFrame:
    """
    Clean and normalize the `job_description` column by removing tab and newline characters.

    :param data: DataFrame containing a column `job_description` as string data
    :return: The modified DataFrame where tab and newline characters are removed.
    """
    data["job_description"] = data["job_description"].str.replace(pat="\r", repl="")
    data["job_description"] = data["job_description"].str.replace(pat="\n", repl="")
    data["job_description"] = data["job_description"].str.replace(pat="\t", repl="")
    return data


def extract_publication_date_from_other_info_column(data: DataFrame) -> DataFrame:
    """
    Extract the publication date from the `job_other_info` column using a predefined
    regular expression pattern and add it as a new column called `publication_date`.

    :param data: DataFrame containing a column `job_other_info` column, where the
        publication date may be embedded within other job-related information.
    :return: The modified DataFrame with an additional `publication_date` column
        containing the extracted publication date. If no match is found, the
        corresponding cell will be NaN.
    """
    data["publication_date"] = data["job_other_info"].str.extract(
        pat=constants.PUBLICATION_DATE_PATTERN, expand=False
    )
    return data


def normalized_publication_date_column(data: DataFrame):
    """
    Clean and normalize the `publication_date` column attending to
    yyyy-mm-dd format.
    :param data: DataFrame containing a column `publication_date` as string data.
    :return: The modified DataFrame where `publication_date` is normalized.
    """
    data["publication_date"] = pandas.to_datetime(data['publication_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    return data


def extract_job_city_from_other_info_column(data: DataFrame) -> DataFrame:
    """
    Extract the job city from the `job_other_info` column using a predefined
    regular expression pattern and add it as a new column called `city`.

    :param data: DataFrame containing a column `job_other_info` column, where the
        job city may be embedded within other job-related information.
    :return: The modified DataFrame with an additional `city` column containing
        the extracted job city. If no match is found, the corresponding cell will
        be NaN.
    """
    data["city"] = data["job_other_info"].str.extract(
        pat=constants.CITIES_PATTERN, expand=False
    )
    return data


def extract_workplace_location_from_other_info_column(data: DataFrame) -> DataFrame:
    """
    Extract the workplace location type from the `job_other_info` column using a predefined
    regular expression pattern and add it as a new column called `workplace_location`.

    :param data: DataFrame containing a column `job_other_info` column, where the
        workplace location may be embedded within other job-related information.
    :return: The modified DataFrame with an additional `workplace_location` column
        containing the extracted workplace location type. If no match is found,
        the corresponding cell will be NaN.
    """
    data["workplace_location"] = data["job_other_info"].str.extract(
        pat=constants.WORKPLACE_LOCATION_PATTERN, expand=False
    )
    return data

def normalized_workplace_location_column(data: DataFrame) -> DataFrame:
    """
    Clean and normalize the `workplace_location` column attending to next predefined values:
        - Remoto
        - Híbrido
        - Presencial
    :param data: DataFrame containing a column `workplace_location` as string data.
    :return: The modified DataFrame where `workplace_location` is normalized.
    """
    replacements = {
        "remoto": "Remoto",
        "hibrido": "Híbrido",
        "Hibrido": "Híbrido",
        "híbrido": "Híbrido",
        "presencial": "Presencial"
    }
    data["workplace_location"] = data["workplace_location"].replace(replacements, regex=True)
    return data
    

def extract_updated_value_from_other_info_column(data: DataFrame) -> DataFrame:
    """
    Extract the workplace location type from the `job_other_info` column using a predefined
    regular expression pattern and add it as a new column called `workplace_location`.

    :param data: DataFrame containing a column `job_other_info` column, where the
        workplace location may be embedded within other job-related information.
    :return: The modified DataFrame with an additional `workplace_location` column
        containing the extracted workplace location type. If no match is found,
        the corresponding cell will be NaN.
    """
    data["has_been_updated"] = data["job_other_info"].str.contains(pat=constants.HAS_BEEN_UPDATED_PATTERN, regex=False)
    return data
    
    
def extract_salary_band_from_other_info_column(data: DataFrame) -> DataFrame:
    """
    Extract the salary band from the `job_other_info` column using a predefined
    regular expression pattern and add it as a new column called `salary_band`.

    :param data: DataFrame containing a column `job_other_info` column, where the
        salary band may be embedded within other job-related information.
    :return: The modified DataFrame with an additional `salary_band` column
        containing the extracted salary band. If no match is found, the corresponding
        cell will be NaN.
    """
    data["salary_band"] = data["job_other_info"].str.findall(constants.SALARY_BAND_PATTERN)
    return data


def normalize_salary_band(data: DataFrame) -> DataFrame:
    """
    Extract the salary lower and upper band from the `salary_band` by index.

    :param data: DataFrame containing a column `salary_band` column, where the
        lower and upper salary band may be embedded.
    :return: The modified DataFrame with two additional `salary_lower_bound` and
        `salary_upper_bound` columns containing the lower and the upper salary band
        respectively. If no match is found, the corresponding cell will be NaN.
    """
    aux_df = DataFrame(
        data['salary_band'].tolist(), columns=['salary_lower_bound', 'salary_upper_bound']
    )
    data["salary_lower_bound"] = aux_df["salary_lower_bound"]
    data["salary_upper_bound"] = aux_df["salary_upper_bound"]
    return data


def normalized_salary_column(data: DataFrame) -> DataFrame:
    """
    Clean and normalize `salary_lower_bound` and `salary_upper_bound` columns by
    removing '€' and '.' characters

    :param data: DataFrame containing both `salary_lower_bound` and `salary_upper_bound`
        as string data.
    :return: The modified DataFrame where `salary_lower_bound` and `salary_upper_bound`
        are normalized and casted to float type.
    """
    data["salary_lower_bound"] = data["salary_lower_bound"].str.replace(pat="€", repl="")
    data["salary_lower_bound"] = data["salary_lower_bound"].str.replace(pat=".", repl="").astype(float)
    data["salary_upper_bound"] = data["salary_upper_bound"].str.replace(pat="€", repl="")
    data["salary_upper_bound"] = data["salary_upper_bound"].str.replace(pat=".", repl="").astype(float)
    return data


def add_current_date_column(data: DataFrame) -> DataFrame:
    """
    Add `cutoff_date` column including current execution date.

    :param data: DataFrame that not include the current execution date information
    :return: The modified DataFrame with an additional `cutoff_date` column
        containing the current execution date.
    """
    data["cutoff_date"] = datetime.now().strftime("%Y-%m-%d")
    return data


def drop_aux_columns(data: DataFrame) -> DataFrame:
    """
    Drop unnecessary columns:
        - `job_other_info`
        - `salary_band`
    :param data: DataFrame with extra unnecessary information.
    :return: The modified DataFrame without `job_other_info` and `salary_band` columns.
    """
    data.drop(labels=["job_other_info", "salary_band"], axis="columns", inplace=True)
    return data


def transformations(data: DataFrame) -> DataFrame:
    """
    Transformations:
        - Normalized `job_description`.
        - Extract and normalized `publication_date` from `other_info_column`.
        - Extract `city` from `other_info_column`.
        - Extract and normalized `workplace_location` from `other_info_column`.
        - Extract `has_been_updated` from `other_info_column`.
        - Extract and normalized `salary_lower_bound` from `other_info_column`.
        - Extract and normalized `salary_upper_bound` from `other_info_column`.
        - Add `cutoff_date`.
        - Drop `job_other_info` and `salary_band`.
    :param data: Dataframe with raw data.
    :return: The modified Dataframe.
    """
    logger.info(f"Transforming Description column")
    data = normalized_job_description_column(data)
    logger.info(f"Transforming Publication Date column")
    data = extract_publication_date_from_other_info_column(data)
    data = normalized_publication_date_column(data)
    logger.info(f"Transforming Job City column")
    data = extract_job_city_from_other_info_column(data)
    logger.info(f"Transforming Workplace Location column")
    data = extract_workplace_location_from_other_info_column(data)
    data = normalized_workplace_location_column(data)
    logger.info(f"Transforming Updated Value column")
    data = extract_updated_value_from_other_info_column(data)
    logger.info(f"Transforming Salary Band column")
    data = extract_salary_band_from_other_info_column(data)
    data = normalize_salary_band(data)
    data = normalized_salary_column(data)
    logger.info(f"Adding Current Date column")
    data = add_current_date_column(data)
    logger.info(f"Dropping unnecessary columns")
    data = drop_aux_columns(data)
    return data
