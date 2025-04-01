# enter word/statement
word = input("Enter a word: ")

# enter the text to find
substring = input("Enter the word/statement to find: ")

# find the last occurrence
position = word.rfind(substring)

# print result
if position != -1:
    print(f'The substring "{substring}" last appears at index {position}.')
else:
    print("Raising ValueError")