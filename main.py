Task 1: Print all words beginning with ‘c’

# Input string
sentence = "People with courage and character always seem to have the beautiful birds on their side."

# Split the sentence into words
words = sentence.split()

# Filter and print words starting with 'c'
words_starting_with_c = [word.strip(",.'") for word in words if word.lower().startswith('c')]

print("Words starting with 'c':")
for word in words_starting_with_c:
    print(word)

Task 2: Check if the string is ASCII

# Input string
sentence = "People with courage and character always seem to have the beautiful birds on their side."

# Check if the string is ASCII
is_ascii = all(ord(char) < 128 for char in sentence)

# Print the result
print("Is the string ASCII?", is_ascii)
