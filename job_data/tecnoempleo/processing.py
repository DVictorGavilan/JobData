from pandas import DataFrame
from datetime import datetime


PUBLICATION_DATE_PATTERN: str = r"([0-9]{0,2}[/][0-9]{0,2}[/][0-9]{0,4})"
WORKPLACE_LOCATION_PATTERN: str = r"(remoto|presencial|Hibrido|hibrido|híbrido|Híbrido)"
HAS_BEEN_UPDATED_PATTERN: str = r"(Actualizada)"
SALARY_BAND_PATTERN: str = r"[0-9]{0,3}[.][0-9]{0,3}[€]"


def normalized_job_name_column(data: DataFrame) -> DataFrame:
    data["job_name"] = data["job_name"].str.replace(pat="Urgente", repl="")
    data["job_name"] = data["job_name"].str.replace(pat="\t\t", repl="")
    data["job_name"] = data["job_name"].str.replace(pat="\t", repl="")
    data["job_name"] = data["job_name"].str.replace(pat=" ", repl="")
    data["job_name"] = data["job_name"].str.replace(pat="\n", repl="")
    return data


def normalized_job_description_column(data: DataFrame) -> DataFrame:
    data["job_description"] = data["job_description"].str.replace(pat="\t", repl="")
    data["job_description"] = data["job_description"].str.replace(pat="\n", repl="")
    return data


def normalized_other_info_column(data: DataFrame) -> DataFrame:
    data["publication_date"] = data["job_other_info"].str.extract(PUBLICATION_DATE_PATTERN, expand=False)
    data["workplace_location"] = data["job_other_info"].str.extract(WORKPLACE_LOCATION_PATTERN, expand=False)
    data["has_been_updated"] = data["job_other_info"].str.extract(HAS_BEEN_UPDATED_PATTERN, expand=False)
    data["salary_band"] = data["job_other_info"].str.findall(SALARY_BAND_PATTERN)
    return data


def extract_salary_band(data: DataFrame) -> DataFrame:
    aux_df = DataFrame(data['salary_band'].tolist(), columns=['salary_lower_bound', 'salary_upper_bound'])
    data["salary_lower_bound"] = aux_df["salary_lower_bound"]
    data["salary_upper_bound"] = aux_df["salary_upper_bound"]
    return data


def normalized_salary_column(data: DataFrame) -> DataFrame:
    data["salary_lower_bound"] = data["salary_lower_bound"].str.replace(pat="€", repl="")
    data["salary_lower_bound"] = data["salary_lower_bound"].str.replace(pat=".", repl="")
    data["salary_upper_bound"] = data["salary_upper_bound"].str.replace(pat="€", repl="")
    data["salary_upper_bound"] = data["salary_upper_bound"].str.replace(pat=".", repl="")
    return data


def add_current_date_column(data: DataFrame) -> DataFrame:
    data["cutoff_date"] = datetime.now().strftime("%Y-%m-%d")
    return data


def drop_aux_columns(data: DataFrame) -> DataFrame:
    data.drop(labels=["job_other_info", "salary_band"], axis="columns", inplace=True)
    return data


def transformations(data: DataFrame) -> DataFrame:
    # data = normalized_job_name_column(data)
    data = normalized_job_description_column(data)
    data = normalized_other_info_column(data)
    data = extract_salary_band(data)
    data = normalized_salary_column(data)
    data = add_current_date_column(data)
    data = drop_aux_columns(data)
    return data
