# enter word/statement
word = input("Enter a statement: ")

# make the first letter capital and the rest lowercase
if len(word) > 0:
    capitalized = word[0].upper() + word[1:].lower()
else:
    capitalized = word

# print result
print(f"Output: {capitalized}")