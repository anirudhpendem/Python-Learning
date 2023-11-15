# Missing authentication for critical function

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import re


def csrf_token(input_string):
    csrf_token_pattern = r'name=["\']?(\w+[\-_]?token)\b["\']?[^>]*\svalue=["\'](.*?)["\']'
    matches = re.findall(csrf_token_pattern, input_string)
    if matches:
        token_dict = {}
        for match in matches:
            name, token = match
            token_dict[name] = token
        return token_dict

def crawl_and_classify(login_url, form_data):
    response = session.get(login_url, allow_redirects=True)
    input_string = response.text
    csrf = csrf_token(input_string)
    if csrf:
        form_data.update(csrf)
        login_response = session.post(login_url, data=form_data, allow_redirects=True)
        url = login_response.url
        path_info = urlparse(url)
        baseurl = path_info.scheme + "://" + path_info.netloc
        
        if login_response.status_code == 200:
            soup = BeautifulSoup(login_response.text, 'html.parser')
            for links in soup.find_all("a", href=True):
                link = links.get("href")
                if link:
                    if "admin" in link:
                        admin_urls.add(baseurl + link)
                    elif ("http" not in link) and ("https" not in link):
                            user_urls.add(baseurl + link)


final_list = []
error_list = []
admin_urls = set()
user_urls = set()

try:
    session = requests.Session()
    timestamp = datetime.now().strftime("%c")
    
    admin_login_url = 'http://128.199.25.82:8096/adminlogin'
    user_login_url = 'http://128.199.25.82:8096/patientlogin'
    
    admin_form_data = {
        "username": 'admin',
        "password": 'admin',
    }
    
    user_form_data = {
        "username": 'peter',
        "password": 'peter',
    }
    
    crawl_and_classify(admin_login_url, admin_form_data)

    crawl_and_classify(user_login_url, user_form_data)

    session.close()

    for i in user_urls:
        final_response = requests.get(i)
        if final_response.status_code == 200:
            final_list.append({"Url":i,"Status_code":final_response.status_code,"Status":"False","Request_headers":dict(final_response.request.headers),"Response_headers":dict(final_response.headers),"Timestamp":timestamp})
        else:
            final_list.append({"Url":url,"Status_code":final_response.status_code,"Status":"True","Request_headers":dict(final_response.request.headers),"Response_headers":dict(final_response.headers),"Timestamp":timestamp})

except Exception as e:
    fdict = {"error": f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}"}
    error_list.append(fdict)

print(json.dumps([final_list,error_list]))