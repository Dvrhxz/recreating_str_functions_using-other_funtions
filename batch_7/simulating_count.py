# enter word/statement
word = input("Enter a word: ")

# enter the text to count
substring = input("Enter the word/statement to count: ")

# count each time it is iterated
count = 0
start = 0

while True:
    start = word.find(substring, start)

    if start == -1:
        break

    else:
        count += 1
        start += len(substring)

# print result
print(f'The substring "{substring}" appears {count} times in the text.')