from pandas import DataFrame
from datetime import datetime
from job_data import quality, transformation, utils


def processing_job_data(job_data: DataFrame) -> DataFrame:
    # normalized_technologies_name = utils.read_json('config/normalized_names.json')
    quality.check_nulls(job_data, 'nombre_empleo')
    quality.check_nulls(job_data, 'empresa')
    quality.check_nulls(job_data, 'city')
    quality.check_nulls(job_data, 'tecnologias')
    quality.check_nulls(job_data, 'descripcion')
    quality.check_nulls(job_data, 'url')
    job_data['descripcion'] = job_data['descripcion'].str.lower()
    job_data['publication_date'] = job_data['descripcion'].apply(transformation.add_date)
    job_data['salary_range'] = job_data['descripcion'].apply(transformation.extract_salary_amount)
    job_data['salary_min'] = job_data['aux_salary'].apply(transformation.extract_salary_min)
    job_data['salary_max'] = job_data['aux_salary'].apply(transformation.extract_salary_max)
    job_data['modalidad'] = job_data['descripcion'].apply(transformation.extract_modality)
    # job_data['technologies'] = job_data['tecnologias'].apply(transformation.normalized_technologies())
    quality.check_type(job_data, 'aux_salary_min', float)
    quality.check_type(job_data, 'aux_salary_min', float)
    quality.check_type(job_data, 'aux_date', datetime)
    return job_data


def processing_cities_info(cities_info: DataFrame) -> DataFrame:
    quality.check_nulls(cities_info, 'id_city')
    quality.check_nulls(cities_info, 'city')
    quality.check_nulls(cities_info, 'num_ofertas')
    return cities_info
