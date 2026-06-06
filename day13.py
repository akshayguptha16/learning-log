# # import requests

# # response = requests.get("https://jsonplaceholder.typicode.com/users/1")
# # print(response.status_code)
# # print(response.json())

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# # print(response.status_code)
# # print(response.json())

# print(response.json()[0:10])

# # Leanne Graham - Sincere@april.biz
# # Ervin Howell - Shanna@melissa.tv

# for user in response.json():
#     print(user['name'] + " - " + user['email'])
# print(response.json()[0]['name'] + " - " + response.json()[0]['email'])

import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")     # API call to fetch user data
    response.raise_for_status()  # Check if the request was successful
    users = response.json()
    for user in users:
        print(f"{user['name']} - {user['email']}")
except requests.exceptions.ConnectionError :
    print(f"Connection failed ! check your connection.")