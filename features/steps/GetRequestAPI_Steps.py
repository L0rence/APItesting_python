from behave import *
import requests
from bs4 import BeautifulSoup
import json
import configparser
from utilities.configuration import *

config = getConfig()


@given('the employee details needs to be fetch from the API call request')
def get_step_implementation(context):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    context.url = requests.get(config['API']['endpoint'] + '/api/v1/employee/1', headers=headers)


@when('I execute the GetAPI method')
def step_impl(context):
    context.data = context.url.content
    # String format
    context.val_str = context.data.decode('UTF-8')
    # print(context.val_str)


@then('Validate the employee details')
def step_impl(context):
    # convert str_byte into dict
    dict_1 = json.loads(context.val_str)

    print(dict_1['status'])
    assert dict_1['status'] == 'success'

    print(dict_1['data']['id'])
    assert dict_1['data']['id'] == 1, "Numbers not matching"

    print(dict_1['data']['employee_name'])
    assert dict_1['data']['employee_name'] == 'Tiger Nixon', "Name not matching.."

    print(dict_1['data']['employee_salary'])
    assert dict_1['data']['employee_salary'] == 320800, "Salary not matching"

    print(dict_1['data']['employee_age'])
    assert dict_1['data']['employee_age'] == 61, "Age not matching"

    print(dict_1['data']['profile_image'])
    assert dict_1['data']['profile_image'] == ''

    print(dict_1['message'])
    assert dict_1['message'] == 'Successfully! Record has been fetched.'
    print(dict_1['message'])
