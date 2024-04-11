from behave import when, then
import json
import requests
from environment import BASE_URL
from urllib.parse import urljoin
from assertpy import assert_that


@when('I make a "{request_method}" request to the "{endpoint_url}"')
def request_without_payload(context, request_method, endpoint_url):
    request_method = request_method.lower()
    full_endpoint_url = urljoin(BASE_URL, endpoint_url)
    context.response = requests.request(request_method, full_endpoint_url)


@then('response body is matching expected "{expected_response_file}"')
def expected_response_body(context, expected_response_file):
    # Open json file / expected response
    with open(f"features/data/response/{expected_response_file}", "r") as file:
        expected_response = json.load(file)
    # Assert response json is equal to json from a file.
    assert_that(context.response.json()).is_equal_to(expected_response)


@then('the response code is "{expected_status}"')
def expected_status_code(context, expected_status):
    assert_that(context.response.status_code).is_equal_to(int(expected_status))
