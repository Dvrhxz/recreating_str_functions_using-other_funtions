# enter word/statement
word = input("Enter a statement: ")

# enter ending word/statement
ending = input("Enter the ending word: ")

# check if both are the same
if word[len(word) - len(ending):] == ending:
    # print result
    print("The ending of the inputted word matches with the inputted ending.")
else:
    print("The word does not match with the inputted ending.")

