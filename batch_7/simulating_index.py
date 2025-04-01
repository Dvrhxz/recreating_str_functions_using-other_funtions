# enter word/statement
word = input("Enter a word: ")

# enter the text to find
substring = input("Enter the word/statement to find: ")

# find the first occurrence
position = word.find(substring)

# print result
if position != -1:
    print(f'The substring "{substring}" first appears at index {position}.')
else:
    print("Raising ValueError")