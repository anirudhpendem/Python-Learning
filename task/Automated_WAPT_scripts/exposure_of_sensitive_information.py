# Exposure of sensitive information through sent data 

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import re

params = ['DB_USERNAME','DB-USERNAME','USERNAME','Secret','Credit Card','password','creditcard','credit-card','credit_card','access_token_secret','api_secret_key','aws-access_key_id','aws_secret_access_key','bucket','client-secret','dbpasswd','encryption-key','encryption_key','private_key','private-key','secret_key','secret-key','ssh-key','ssh_key','patient name','patient_name','patient-name','disease','health records','bereauId']
params = [each_string.lower() for each_string in params]

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


    for urls in user_urls:
        final_response = session.get(urls)
        response_body = response.content.decode("utf-8")
        for param in params:
            if param in response_body.lower():
                status = "True"
                final_list.append({"Url":urls,"Status_code":final_response.status_code,"Status":status,"Request_headers":dict(final_response.request.headers),"Response_headers":dict(final_response.headers),"Timestamp":timestamp})
            else:
                final_list.append({"Url":urls,"Status_code":final_response.status_code,"Status":"False","Request_headers":dict(final_response.request.headers),"Response_headers":dict(final_response.headers),"Timestamp":timestamp})



except Exception as e:
    fdict = {"error": f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}"}
    error_list.append(fdict)

print(json.dumps([final_list,error_list]))