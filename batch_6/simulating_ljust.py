# enter word/statement
word = input("Enter a word: ")

# enter the length
length = int(input("Enter the length: "))

# add space characters at the end
if len(word) < length:
    word = word + " " * (length - len(word))

# print result
print(f"Output: '{word}'")