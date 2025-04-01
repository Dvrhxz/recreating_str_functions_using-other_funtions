# input a statement/word
word = input("Enter a statement: ")
all_lower = True

# check if all is lower
for character in word:
    if character.isupper():
        all_lower = False


# print result
if all_lower:
    print("All characters are lowercase.")
else:
    print("Not all characters are lowercase.")