import json

filename = './10 FILES AND EXCEPTIONS/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)