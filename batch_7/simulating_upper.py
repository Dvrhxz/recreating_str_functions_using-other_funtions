# input word/statement
word = input("Enter a statement: ")
capitalized_word = ""

# check if input is lower
for character in word:
    # if lower swapcase to upper
    if character.islower():
        capitalized_word += character.swapcase()
    else:
        capitalized_word += character

# print results
print(f"Output: {capitalized_word}")