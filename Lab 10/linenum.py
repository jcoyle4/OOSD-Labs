#   filename = str(input("What file do you want to look in? \n"))
filename = 'dictionary.txt'
index = 1
with open(filename, "r") as f:
    for word in f:
        word = word.rstrip()
        print(index, ":", word)
        index += 1
