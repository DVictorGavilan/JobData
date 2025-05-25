from assertpy import assert_that
from unittest.mock import patch, MagicMock
from job_data.tecnoempleo.scraper import *


HTML_CONTENT = """
    <html>
        <head>
            <title>Job Listings</title>
        </head>
        <body>
            <h1 class='h4 h6-xs text-center my-4'>50 Example City Data, Page 18</h1>
            <div class='p-3 border rounded mb-3 bg-white'>
                <a class='font-weight-bold text-cyan-700' href='http://www.test1.com' title='Job Test 1'></a>
                <a class='text-primary'>Company Test 1</a>
                <span class='badge bg-gray-500 mx-1'>Python</span>
                <span class='badge bg-gray-500 mx-1'>Java</span>
                <span class='hidden-md-down text-gray-800'><br><br>Description Test 1</span>
                <div class='col-12 col-lg-3 text-gray-700 pt-2 text-right hidden-md-down'>Other Info 1</div>
            </div>
            <div class='p-3 border rounded mb-3 bg-white'>
                <a class='font-weight-bold text-cyan-700' href='http://www.test2.com' title='Job Test 2'></a>
                <a class='text-primary'>Company Test 2</a>
                <span class='badge bg-gray-500 mx-1'>Scala</span>
                <span class='badge bg-gray-500 mx-1'>PHP</span>
                <span class='hidden-md-down text-gray-800'><br><br>Description Test 2</span>
                <div class='col-12 col-lg-3 text-gray-700 pt-2 text-right hidden-md-down'>Other Info 2</div>
            </div>
        </body>
    </html>
"""
MOCK_SOUP = BeautifulSoup(markup=HTML_CONTENT, features="html.parser")

MOCK_EMPTY_SOUP = BeautifulSoup(markup="", features="html.parser")


@patch("job_data.tecnoempleo.scraper.requests.get")
def test_successful_connection(mock_get):
    url = "https://example.com"
    mock_response = MagicMock(status_code=200, content=HTML_CONTENT.encode())
    mock_get.return_value = mock_response
    soup = get_html(url=url)
    assert_that(soup).is_instance_of(BeautifulSoup)
    assert_that(soup.find("h1").text).is_equal_to("50 Example City Data, Page 18")


@patch("job_data.tecnoempleo.scraper.requests.get")
def test_unsuccessful_connection(mock_get):
    url = "https://example.com"
    mock_get.side_effect = requests.exceptions.RequestException
    assert_that(get_html).raises(requests.exceptions.RequestException).when_called_with(url)


def test_getting_total_jobs():
    assert_that(get_total_jobs(MOCK_SOUP)).is_equal_to(50)


def test_getting_total_jobs_tag_not_found():
    msg_error = "{'name': 'h1', 'class': {'class': 'h4 h6-xs text-center my-4'}}"
    assert_that(get_total_jobs).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_jobs_div_successful():
    assert_that(get_job_divs(MOCK_SOUP)).is_length(2)
    assert_that(get_job_divs(MOCK_SOUP)).is_instance_of(ResultSet)


def test_get_jobs_div_unsuccessful():
    msg_error = "{'name': 'div', 'class': {'class': 'p-3 border rounded mb-3 bg-white'}}"
    assert_that(get_job_divs).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_name_successful():
    assert_that(get_job_name(MOCK_SOUP)).is_equal_to("Job Test 1")
    assert_that(get_job_name(MOCK_SOUP)).is_instance_of(str)


def test_get_job_name_unsuccessful():
    msg_error = "{'name': 'a', 'class': {'class': 'font-weight-bold text-cyan-700'}}"
    assert_that(get_job_name).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_url_successful():
    assert_that(get_job_url(MOCK_SOUP)).is_equal_to("http://www.test1.com")
    assert_that(get_job_url(MOCK_SOUP)).is_instance_of(str)


def test_get_job_url_unsuccessful():
    msg_error = "{'name': 'a', 'class': {'class': 'font-weight-bold text-cyan-700'}}"
    assert_that(get_job_url).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_company_successful():
    assert_that(get_job_company(MOCK_SOUP)).is_equal_to("Company Test 1")
    assert_that(get_job_company(MOCK_SOUP)).is_instance_of(str)


def test_get_job_company_unsuccessful():
    msg_error = "{'name': 'a', 'class': {'class': 'text-primary'}}"
    assert_that(get_job_company).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_technologies_successful():
    div = get_job_divs(soup=MOCK_SOUP)
    assert_that(get_job_technologies_stack(div[0])).is_equal_to(["Python", "Java"])
    assert_that(get_job_technologies_stack(div[0])).is_instance_of(list)


def test_get_job_technologies_unsuccessful():
    msg_error = "{'name': 'span', 'class': {'class': 'badge bg-gray-500 mx-1'}}"
    assert_that(get_job_technologies_stack).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_description_successful():
    assert_that(get_job_description(MOCK_SOUP)).is_equal_to("Description Test 1")
    assert_that(get_job_description(MOCK_SOUP)).is_instance_of(str)


def test_get_job_description_unsuccessful():
    msg_error = "{'name': 'span', 'class': {'class': 'hidden-md-down text-gray-800'}}"
    assert_that(get_job_description).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_get_job_other_info_successful():
    assert_that(get_job_other_info(MOCK_SOUP)).is_equal_to("Other Info 1")
    assert_that(get_job_other_info(MOCK_SOUP)).is_instance_of(str)


def test_get_job_other_info_unsuccessful():
    msg_error = "{'name': 'div', 'class': {'class': 'col-12 col-lg-3 text-gray-700 pt-2 text-right hidden-md-down'}}"
    assert_that(get_job_other_info).raises(ElementNotFound).when_called_with(MOCK_EMPTY_SOUP).is_equal_to(msg_error)


def test_extract_job_data_successfully():
    expected = {
        "job_url": "http://www.test1.com",
        "job_name": "Job Test 1",
        "job_company": "Company Test 1",
        "job_technologies_stack": ["Python", "Java"],
        "job_description": "Description Test 1",
        "job_other_info": "Other Info 1",
    }
    div = get_job_divs(soup=MOCK_SOUP)
    assert_that(extract_job_data(div[0])).is_equal_to(expected)


@patch("job_data.tecnoempleo.scraper.get_html")
def test_download_job_data_successfully(mock_get_html):
    expected = [
        {
            "job_url": "http://www.test1.com",
            "job_name": "Job Test 1",
            "job_company": "Company Test 1",
            "job_technologies_stack": ["Python", "Java"],
            "job_description": "Description Test 1",
            "job_other_info": "Other Info 1"
        },
        {
            "job_url": "http://www.test2.com",
            "job_name": "Job Test 2",
            "job_company": "Company Test 2",
            "job_technologies_stack": ["Scala", "PHP"],
            "job_description": "Description Test 2",
            "job_other_info": "Other Info 2"
        },
        {
            "job_url": "http://www.test1.com",
            "job_name": "Job Test 1",
            "job_company": "Company Test 1",
            "job_technologies_stack": ["Python", "Java"],
            "job_description": "Description Test 1",
            "job_other_info": "Other Info 1"
        },
        {
            "job_url": "http://www.test2.com",
            "job_name": "Job Test 2",
            "job_company": "Company Test 2",
            "job_technologies_stack": ["Scala", "PHP"],
            "job_description": "Description Test 2",
            "job_other_info": "Other Info 2"
        }
    ]
    mock_get_html.return_value = MOCK_SOUP
    assert_that(download_job_data()).is_equal_to(expected)
