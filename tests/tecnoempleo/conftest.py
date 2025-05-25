import pytest

from numpy import nan
from pandas import DataFrame
from datetime import datetime
from job_data.tecnoempleo.processing import transformations


@pytest.fixture
def mock_raw_data():
    return DataFrame({
        "job_url": ["http://www.test1.com", "http://www.test2.com"],
        "job_name": ["Job Test 1", "Job Test 2"],
        "job_company": ["Company Test 1", "Company Test 2"],
        "job_technologies_stack": [["Python", "Java"], ["Scala", "PHP"]],
        "job_description": ["\nDescription Test \n\t1", "\t\tDescription Test 2"],
        "job_other_info": ["15/12/2024Madrid(remoto)Actualizada16.000€ - 18.000€ b/a", "11/11/2011Barcelona(hibrido) - 20.000€ b/a"],
    })


@pytest.fixture
def mock_master_expected_data():
    return DataFrame({
        "job_url": ["http://www.test1.com", "http://www.test2.com"],
        "job_name": ["Job Test 1", "Job Test 2"],
        "job_company": ["Company Test 1", "Company Test 2"],
        "job_technologies_stack": [["Python", "Java"], ["Scala", "PHP"]],
        "job_description": ["Description Test 1", "Description Test 2"],
        "publication_date": ["2024-12-15", "2011-11-11"],
        "city": ["Madrid", "Barcelona"],
        "workplace_location": ["Remoto", "Híbrido"],
        "has_been_updated": [True, False],
        "salary_lower_bound": [16000., 20000.],
        "salary_upper_bound": [18000., nan],
        "cutoff_date": [datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%Y-%m-%d")]
    })


@pytest.fixture
def mock_master_actual_data(mock_raw_data):
    return transformations(mock_raw_data)
