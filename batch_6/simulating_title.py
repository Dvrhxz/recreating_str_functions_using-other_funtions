# enter word/statement
statement = input("Enter a statement: ")

# make the first letter of each word capital and the rest lowercase
words = statement.split()
titled_word = []
for word in words:
    if len(word) > 0:
        formatted_word = word[0].upper() + word[1:].lower()
        titled_word.append(formatted_word)

# join the words into a single string with spaces
titled_word = ' '.join(titled_word)

# print result
print(f"Output: {titled_word}")