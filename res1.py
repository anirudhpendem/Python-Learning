import requests

from requests.exceptions import HTTPError

uri = input('Enter the a valid URI:\n')

print('Waiting for the response...\n')

try:

    response = requests.get(uri)

    response.raise_for_status()

    jsonResponse = response.json()

    print("The JSON content is: \n")

    for key, value in jsonResponse.items():

        print(key, ":", value)

except HTTPError as http_err:

    print('HTTP error occurred: %s' %http_err)

except Exception as err:

    print('Other error occurred: %s' %err)