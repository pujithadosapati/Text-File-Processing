from io import StringIO
#  Create sample text in memory
text = """Python is a programming language.
File handling is useful.
I am learning Python."""
# Read and process the text
file = StringIO(text)
line_count = 0
word_count = 0
character_count = 0
for line in file:
    line_count += 1
    word_count += len(line.split())
    character_count += len(line)
#  Display statistics
print("===== TEXT FILE STATISTICS =====")
print("File Name: sample.txt")
print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", character_count)
