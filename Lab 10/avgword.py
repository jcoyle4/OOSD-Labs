#   filename = str(input("What file do you want to look in? \n"))
filename = 'dictionary.txt'
amount_of_words = 0
length_of_words = 0
average_numerator = 0

with open(filename, "r") as f:
    for word in f:
        amount_of_words += 1
        #   word = word.lstrip()    #   Removes leading whitespace
        word = word.rstrip()    #   Removes trailing whitespace
        length_of_words += len(word)

average = length_of_words / amount_of_words

print("There are this many words:", amount_of_words)
print("There are this many letters:", length_of_words)
print("The average length of the words is", round(average, 2))
