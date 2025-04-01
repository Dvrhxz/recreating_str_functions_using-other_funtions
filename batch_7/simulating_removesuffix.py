# input word/statement
statement = input("Enter a statement: ")

# input suffix
suffix =  input("enter a suffix to remove: ")

# remove the inputted suffix from the word/statement
if statement.endswith(suffix):
    statement = statement[:len(statement) - len(suffix)]

# print results
print(f"Output: {statement}")