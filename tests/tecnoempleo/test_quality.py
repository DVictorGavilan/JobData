from assertpy import assert_that
from job_data.tecnoempleo.quality import minimum_data_quality_expected


def test_minimum_data_quality_expected_exceeded(master_expected_data):
    assert_that(minimum_data_quality_expected(master_expected_data)).is_false()
