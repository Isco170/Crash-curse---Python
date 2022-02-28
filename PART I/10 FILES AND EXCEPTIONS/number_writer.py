import json

numbers = [2, 3, 5, 7, 11, 13]

filename = './10 FILES AND EXCEPTIONS/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

