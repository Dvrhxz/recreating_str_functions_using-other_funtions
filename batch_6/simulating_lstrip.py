# enter word/statement with spaces
word = input("Enter a word: ")

# loops through each character
# if it starts with space increment by one until there is a valid character in that index
character = 0

while character < len(word) and word[character] == " ":
    character += 1

# if the while loop reaches index with valid character, print starting from that point
print(f"Output: {word[character:]}")