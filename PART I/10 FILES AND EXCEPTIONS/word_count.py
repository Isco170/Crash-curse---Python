def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['./10 FILES AND EXCEPTIONS/alice.txt', './10 FILES AND EXCEPTIONS/siddhartha.txt', './10 FILES AND EXCEPTIONS/moby_dick.txt', './10 FILES AND EXCEPTIONS/little_women.txt']

for filename in filenames:
    count_words(filename)
