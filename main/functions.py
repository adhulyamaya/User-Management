import string
import random
import requests

# def get_user_token(request, user_name, password):
#     headers = {'Content-Type': 'application/json', }
#     data = '{"username": "' + user_name + '", "password":"' + password + '"}'
#     # print(data, "--data")
#     protocol = "http://"
#     if request.is_secure():
#         protocol = "https://"

#     web_host = request.get_host()
#     request_url = protocol + web_host + "/api/v1/auth/token/"

#     print(request_url, "--------request_url")

#     response = requests.post(request_url, headers=headers, data=data)
#     print(response, "------response2")
#     return (response)
    

def get_user_token(request, user_name, password):
    # Don't concatenate strings to create JSON - vulnerable to injection
    # data = '{"username": "' + user_name + '", "password":"' + password + '"}'  # BAD
    
    # Instead, use:
    data = {
        "username": user_name,
        "password": password
    }
    headers = {'Content-Type': 'application/json'}
    
    # Build URL using urljoin
    from urllib.parse import urljoin
    base_url = f"{'https' if request.is_secure() else 'http'}://{request.get_host()}"
    request_url = urljoin(base_url, "/api/v1/auth/token/")
    
    return requests.post(request_url, headers=headers, json=data)