import requests

response = requests.get('https://api.github.com/')

if response:

    print('The status code of the response is %d' %response.status_code)

    print('The JSON content is: \n%s' %response.json())

    print('\nThe request is handled successfully.')

else:

    print('Invalid response.')