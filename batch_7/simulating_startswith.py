# enter word/statement
word = input("Enter a statement: ")

# enter starting word/statement
start = input("Enter the starting word: ")

# check if both are the same
if word[:len(start)] == start:
    # print result
    print("The start of the inputted word matches with the inputted starting word.")
else:
    print("The word does not match with the inputted start.")