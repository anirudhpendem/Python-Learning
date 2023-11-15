# Sensitive Cookie with Improper SameSite Attribute

import requests
import json
import re
import Authorization_token
import sys
import ast
import urllib3
import urllib
import calendar
import time
import login_script
import getheaders
import full_requests
import random
import string
import linecache
import centralized_data_load
from urllib.parse import urlencode
from urllib.parse import urlparse
from datetime import datetime
from requests.structures import CaseInsensitiveDict
from centralized_data_load import Centralized
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def csrf_token(response_body):

	csrf_token_pattern = r'name=["\']?(\w+[\-_]?token)\b["\']?[^>]*\svalue=["\'](.*?)["\']'
	matches = re.findall(csrf_token_pattern, response_body)
	if matches:
		token_dict = {}
		for match in matches:
			name, token = match
			token_dict[name]=token
		return token_dict
	else:
		final_list.append({"Url":url,"Status_code":response.status_code,"Timestamp":timestamp})


final_list = []
error_list = []

url = "http://128.199.25.82:8096/adminlogin"
# url = "https://enprobe.io/users/sign_in"
login_data = {"username": "admin","password": "admin"}

try:
	timestamp = datetime.now().strftime("%c")
	session = requests.Session()
	response = session.get(url,json = login_data)
	
	if response.status_code == 200:
		response_body = response.content.decode("utf-8")
		csrf_token = csrf_token(response_body)
		# print(csrf_token)
		res = session.get(url,data = csrf_token)
		res_body = res.content.decode("utf-8")
		
		if 'Set-Cookie' in res.headers:
			cookie_header = res.headers['Set-Cookie']

			if "SameSite=None" in cookie_header:
				status = "False"
				final_list.append({"Url":url,"Status_code":response.status_code,"Status":status,"Request_headers":dict(res.request.headers),"Response_headers":dict(res.headers),"Timestamp":timestamp})	
			else:
				status = "True"
				final_list.append({"Url":url,"Status_code":response.status_code,"Status":status,"Request_headers":dict(res.request.headers),"Response_headers":dict(res.headers),"Timestamp":timestamp})
				


except Exception as e:
    fdict = {}
    fdict.update({"error":f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}"}) 
    error_list.append(fdict)
print(json.dumps([final_list,error_list]))