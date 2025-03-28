# input a statement
statement = input("Enter a statement: ")

# input a prefix
prefix =  input("enter a prefix to remove: ")

# remove prefix from statement without .removeprefix()
if statement.startswith(prefix):
    statement = statement[len(prefix):]

# print output
print(f"Results: {statement}")