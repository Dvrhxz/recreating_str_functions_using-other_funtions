# enter word/statement
word = input("Enter a word: ")

# enter the length
length = int(input("Enter the length: "))

# add space characters at the start
if len(word) < length:
    word = " " * (length - len(word)) + word

# print result
print(f"Output: '{word}'")