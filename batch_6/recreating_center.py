# enter word/statement
word = input("Enter a statement: ")

# enter the length
length = int(input("Enter the length: "))

# add space characters at the beginning and end
if len(word) < length:
    total_spaces = length - len(word)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    word = ' ' * left_spaces + word + ' ' * right_spaces

# print result
print(f"Output: '{word}'")