

import requests

response = requests.get(

    'https://api.github.com/search/repositories',

    params={'q': 'requests+language:perl'},

)

if response:

    json_response = response.json()

    repository = json_response['items'][0]

    print(response.json())

   # print('Repository name: %s' %repository["name"])

    #print('Repository description: %s' %repository["description"])

else:

    print('Invalid response.')
