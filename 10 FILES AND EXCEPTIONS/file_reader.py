# with open('./10 FILES AND EXCEPTIONS/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

filename = './10 FILES AND EXCEPTIONS/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)