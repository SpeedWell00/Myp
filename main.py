Task 1: Print all words with exactly 3 letters

# Input string
sentence = "Every day may not be good, but there's something good in every day."

# Split the sentence into words
words = sentence.split()

# Filter words with exactly 3 letters
three_letter_words = [word.strip(",.'") for word in words if len(word.strip(",.'")) == 3]

# Print the result
print("Words with exactly 3 letters:")
print(three_letter_words)
Task 2: Convert the entire string into capital letters

# Input string
sentence = "Every day may not be good, but there's something good in every day."

# Convert the string to uppercase
uppercase_sentence = sentence.upper()

# Print the result
print("Uppercase sentence:")
print(uppercase_sentence)
