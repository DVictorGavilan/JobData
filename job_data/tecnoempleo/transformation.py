import pandas
from pandas import DataFrame


# df = pandas.read_csv("../../data/raw/cities_data_2024-07-23.csv", sep=";")
# print(sum(df["total_num_of_jobs"].tolist()))
# print(pandas.read_csv("../../data/raw/job_data_2024-07-23.csv", sep=";").shape)
# print(pandas.read_csv("../../data/raw/job_data_2024-07-23.csv", sep=";").head().to_string())

job_data = pandas.read_csv("../../data/raw/job_data_2024-07-23.csv", sep=";")

print(job_data.head().to_string())
