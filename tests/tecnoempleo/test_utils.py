from assertpy import assert_that
from job_data.tecnoempleo.utils import *


def test_calculate_total_pages_num_zero_jobs():
    total_pages = calculate_total_pages_num(0)
    assert_that(total_pages).is_equal_to(range(1, 1))


def test_calculate_total_pages_num_boundary_before_next():
    total_pages = calculate_total_pages_num(59)
    assert_that(total_pages).is_equal_to(range(1, 3))


def test_calculate_total_pages_num_boundary_at_next():
    total_pages = calculate_total_pages_num(60)
    assert_that(total_pages).is_equal_to(range(1, 3))


def test_calculate_total_pages_num_boundary_after_next():
    total_pages = calculate_total_pages_num(61)
    assert_that(total_pages).is_equal_to(range(1, 4))
