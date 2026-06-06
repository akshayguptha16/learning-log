
import json
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()  # Check if the request was successful

    filtered_posts = [post for post in response.json() if post['userId'] == 1]

    for post in filtered_posts:
        print(f"Title: {post['title']}\n")

    with open('filtered_posts.json', 'w') as file:
        json.dump(filtered_posts, file, indent=4)

except requests.exceptions.ConnectionError:
    print("Connection failed! Check your connection.")
except requests.exceptions.HTTPError:
    print(f"HTTP error occurred: {response.status_code}")
