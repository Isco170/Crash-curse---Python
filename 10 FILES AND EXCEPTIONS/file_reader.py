# with open('./10 FILES AND EXCEPTIONS/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

filename = './10 FILES AND EXCEPTIONS/pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

# Making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

