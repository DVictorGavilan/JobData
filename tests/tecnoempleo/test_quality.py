from assertpy import assert_that
from job_data.tecnoempleo.quality import minimum_data_quality_expected


def test_minimum_data_quality_expected_exceeded(mock_master_expected_data):
    assert_that(minimum_data_quality_expected(mock_master_expected_data)).is_false()
