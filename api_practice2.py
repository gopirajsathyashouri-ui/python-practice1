import requests 

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

print("Total posts:", len(posts))
count = 0
for post in posts:
    if post["userId"] == 3:
        count += 1

print("Posts by userId 3:", count)