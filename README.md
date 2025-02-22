# JobData

## Functional Description
The goal of this project is to create a Python-based system for aggregating job information from various job boards, executing an ETL (Extract, Transform, Load) process for further analysis and utilization.

## Owner
For any bugs or questions, please reach out to [Dani Gavilán](mailto:danigavipedro96@gmail.com).

## Branching Methodology
This project follows a Git Flow simplified branching methodology
- **Master Branch**: production code
- **Develop Branch**: main integration branch for ongoing development. Features and fixes are merged into this branch before reaching master
- **Feature Branch**: created from develop branch to work on new features

## Prerequisites
This project uses:
- Language: Python 3.10
- Libraries: 
  - beautifulsoup4
  - pandas
  - data_quality-kit
  - pytest & pytest-cov
  - assertpy

## How to use it
Install dependencies and run:

```bash
python main.py
```


## How it works
### Extraction
The script begins by performing web scraping on the target pages, utilizing various HTML tags to extract the necessary information. The output is formatted as a JSON-like structure adapted for Python—a list of dictionaries. However, the data is stored in a DataFrame for the subsequent steps.
### Transformations
Once the raw information is downloaded, transformations are applied to clean the data. These include operations such as replace, split, format modification, and adding or removing fields.
### Data Quality Validations
Using the DataQualityKit library, a series of validations are applied to the DataFrame to ensure minimum data quality. This includes validation rules for missing values, among others.
### Load
Finally, if the data meets the minimum quality requirements, it is stored in both the raw and master zones for future use.
### Logging
The project structure is designed to be executed periodically. As a result, it generates an accumulated log of execution results, detailing each run and providing necessary information for debugging if needed.
 