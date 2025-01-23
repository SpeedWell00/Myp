Task 1: Split the line by spaces and print each word on a new line

# Input line
line1 = "Our technology forces us to live mythically, but we continue to think fragmentarily, and on single, separate, and mechanical levels. - Marshall McLuhan"

# Split the line by spaces and print each word on a new line
words = line1.split()
for word in words:
    print(word)

Task 2: Find the number of occurrences of the word “technology”

# Input line
line2 = "We've arranged a civilization in which most crucial elements profoundly depend on science and technology. - Carl Sagan"

# Count occurrences of the word "technology"
word_count = line2.lower().split().count("technology")

# Print the result
print("The word 'technology' appears", word_count, "time(s).")
