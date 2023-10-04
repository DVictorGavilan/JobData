import pandas as pd

from job_data import quality, transformation


def count_repeated_values(elements: list) -> dict:
    return {element: elements.count(element) for element in set(elements)}


data_job = pd.read_csv('data/empleos_info_2023-09-30.csv', sep=';')

# for column in data_job.columns:
#    quality.check_nulls(data_job, columna=column)

# data_job['aux_date']        = data_job['descripcion'].apply(transformation.add_date)
# data_job['aux_descripcion'] = data_job['descripcion'].apply(transformation.add_separate_description)
# data_job['new_tecnologies'] = data_job['tecnologias'].apply(
#     transformation.add_list_technologies)
data_job['aux_salary'] = data_job['descripcion'].apply(transformation.extract_salary_amount)
print(data_job['aux_salary'].head(30))
# print(data_job[['aux_date', 'aux_descripcion']].head().to_string())
# technologies = [technology.lower() for technologies in data_job['new_tecnologies'].to_list()
#                 for technology in technologies]
# technologies = []

# for technologies in data_job['new_tecnologies'].to_list():
#   for technology in technologies:
#      technologies.append(technology.lower())

# for tech, n in count_repeated_values(technologies).items():
#     if 'py' in tech:
#         print(tech, n)

# print(len(technologies))
# print(len(set(technologies)))
# print(len(set([technology.lower() for technology in technologies])))
