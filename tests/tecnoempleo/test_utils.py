from itertools import count
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


def test_generate_base_url_for_default_page():
    expected = "https://www.tecnoempleo.com/ofertas-trabajo/?pagina=1"
    assert_that(generate_base_url()).is_equal_to(expected)


def test_generate_base_url_for_specific_page():
    expected = "https://www.tecnoempleo.com/ofertas-trabajo/?pagina=5"
    assert_that(generate_base_url(5)).is_equal_to(expected)


def test_generate_url_for_a_specific_city_and_default_page():
    expected = "https://www.tecnoempleo.com/busqueda-empleo.php?pr=232&pagina=1"
    assert_that(generate_url_for_city_and_page("232")).is_equal_to(expected)


def test_generate_url_for_a_specific_city_and_specific_page():
    expected = "https://www.tecnoempleo.com/busqueda-empleo.php?pr=232&pagina=5"
    assert_that(generate_url_for_city_and_page("232", 5)).is_equal_to(expected)


def test_get_iterator_element_by_valid_index():
    iterator = iter([10, 20, 30, 40])
    actual = get_iterator_element_by_index(iterator, 2)
    assert_that(actual).is_equal_to(30)


def test_get_iterator_element_by_index_out_of_range():
    iterator = iter([10, 20, 30, 40])
    actual = get_iterator_element_by_index(iterator, 10)
    assert_that(actual).is_none()


def test_get_iterator_element_by_index_in_an_empty_iterator():
    iterator = iter([])
    actual = get_iterator_element_by_index(iterator, 2)
    assert_that(actual).is_none()


def test_iterator_consumption_after_get_iterator_element_by_index():
    iterator = iter([10, 20, 30, 40])
    get_iterator_element_by_index(iterator, 2)
    actual = next(iterator)
    assert_that(actual).is_equal_to(40)
