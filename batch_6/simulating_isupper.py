# Input word/statement
word = input("Enter a statement: ")
all_upper = True

# Check if word is upper or not
for character in word:
    if character.islower():
        all_upper = False

# Print result if all isupper or not
if all_upper:
    print("All characters are uppercase.")
else:
    print("Not all characters are uppercase.")