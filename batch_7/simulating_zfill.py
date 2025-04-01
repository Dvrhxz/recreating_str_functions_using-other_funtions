# enter word/statement/number
word = input("Enter a word: ")

# enter the length
length = int(input("Enter the length: "))

# add 0 at the start
if len(word) < length:
    word = "0" * (length - len(word)) + word

# print result
print(f"Output: '{word}'")