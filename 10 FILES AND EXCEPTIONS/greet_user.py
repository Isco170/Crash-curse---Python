import json

filename = './10 FILES AND EXCEPTIONS/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
