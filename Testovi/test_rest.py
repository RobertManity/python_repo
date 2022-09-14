import requests
import json

def test_get_json():
    url = 'https://api.github.com/users/RobertManity'
    
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.get(url, headers=headers)       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url
    assert resp_body['id'] == 82408792
    assert resp_body['name'] == "Robert Manity"
    # print response full body as text
    print(resp_body)

test_get_json()
