from pandas.testing import assert_series_equal


def test_get_job_description_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["job_description"],
        right=mock_master_expected_data["job_description"]
    )


def test_get_publication_date_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["publication_date"],
        right=mock_master_expected_data["publication_date"]
    )


def test_get_job_city_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["city"],
        right=mock_master_expected_data["city"]
    )


def test_get_workplace_location_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["workplace_location"],
        right=mock_master_expected_data["workplace_location"]
    )


def test_get_updated_value_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["has_been_updated"],
        right=mock_master_expected_data["has_been_updated"]
    )


def test_get_lower_salary_band_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["salary_lower_bound"],
        right=mock_master_expected_data["salary_lower_bound"]
    )


def test_get_upper_salary_band_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["salary_upper_bound"],
        right=mock_master_expected_data["salary_upper_bound"]
    )


def test_get_current_date_successfully(mock_master_actual_data, mock_master_expected_data):
    assert_series_equal(
        left=mock_master_actual_data["cutoff_date"],
        right=mock_master_expected_data["cutoff_date"]
    )
