from numpy import nan
from pandas.testing import assert_series_equal
from job_data.tecnoempleo.processing import *


def test_get_job_description_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["job_description"],
        right=master_expected_data["job_description"]
    )


def test_get_publication_date_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["publication_date"],
        right=master_expected_data["publication_date"]
    )


def test_get_job_city_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["city"],
        right=master_expected_data["city"]
    )


def test_get_workplace_location_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["workplace_location"],
        right=master_expected_data["workplace_location"]
    )


def test_get_updated_value_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["has_been_updated"],
        right=master_expected_data["has_been_updated"]
    )


def test_get_lower_salary_band_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["salary_lower_bound"],
        right=master_expected_data["salary_lower_bound"]
    )


def test_get_upper_salary_band_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["salary_upper_bound"],
        right=master_expected_data["salary_upper_bound"]
    )


def test_get_current_date_successfully(master_actual_data, master_expected_data):
    assert_series_equal(
        left=master_actual_data["cutoff_date"],
        right=master_expected_data["cutoff_date"]
    )
