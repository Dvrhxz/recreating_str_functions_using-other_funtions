# input word/statement
word = input("Enter a statement: ")
lowered_word = ""

# check if word is upper
for character in word:
    if "A" <= character <= "Z":
        # if true, swap case
        lowered_word += character.swapcase()
    else:
        lowered_word += character

# print result
print(f"Output: {lowered_word}")