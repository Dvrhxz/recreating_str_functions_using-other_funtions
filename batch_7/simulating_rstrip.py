# input a word/statement
word = input("Enter a word: ")

# if there are trailing spaces remove them
while len(word) > 0 and word[-1] == " ":
    word = word[:-1]

# print result
print(f"Output: {word}")