# enter word/statement
word = input("Enter a statement: ")

# reverse the casing of each character
result = ""
for char in word:
    # using isupper, islower, lower, and upper
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char

# print result
print(f"Output: {result}")