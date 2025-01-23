# Task 1
# Create and write to file39.txt
with open("file39.txt", "w") as file39:
    file39.write("Python is widely used in artificial intelligence, natural language generation, neural networks, and other advanced fields of computer science.")

# Read file39.txt, replace spaces with underscores, and save to a new file
with open("file39.txt", "r") as file39:
    content = file39.read()
    modified_content = content.replace(" ", "_")

with open("file39_spaces_to_underscore.txt", "w") as new_file:
    new_file.write(modified_content)

# Task 2
# Create and write to file40.txt
with open("file40.txt", "w") as file40:
    file40.write("Python was conceived in the late 1980s as a successor to the ABC language.")

# Read file40.txt, count the letter 'o', and save the result to a new file
with open("file40.txt", "r") as file40:
    content = file40.read()
    o_count = content.count("o")

with open("file40_o_count.txt", "w") as new_file:
    new_file.write(f"Number of 'o' characters: {o_count}")
