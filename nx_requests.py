import json
import requests
import pandas as pd
from requests import urllib3
#from interfaces import RoutedInterface
#from  routing import ospf
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def post(mo_dn, mo, mo_data, apic_url, apic_user, apic_pw):
    # Construct JSON for logon request
    print(mo_data)
    base_url = ('https://%s/api/' % apic_url)
    cookies = {}
    name_pwd = {'aaaUser': {'attributes': {'name': apic_user, 'pwd': apic_pw}}}
    json_credentials = json.dumps(name_pwd)


    # log in to API
    login_url = base_url + 'aaaLogin.json'
    post_response = requests.post(login_url, data=json_credentials, verify=False)
    # get token from login response structure
    auth = json.loads(post_response.text)
    login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
    auth_token = login_attributes['token']
    # create cookie array from token
    cookies['APIC-Cookie'] = auth_token
    sensor_url = (base_url + mo_dn)

    # Convert the class based object into a dictionary and load into JSON format
    post_dict = mo_data.__dict__
    print(post_dict)
    json_post = json.dumps(post_dict)
    get_response = requests.post(sensor_url, data=json_post, cookies=cookies,
    verify=False)
    print(get_response.json())
    # Check for success or failure of the post
    if get_response.status_code == 200:
        print("SUCCESS Posting Object: {}".format(get_response.status_code))

    elif get_response.status_code != 200:
        print("FAILED Posting Object: {}".format(get_response.status_code))
        print('Review the input data and logfile for more detail')
        pause = input('PRESS ANY KEY TO CONTINUE PROCESSING')
    return json_post
