import time

# Creating a dictionary to store the count of each word
word_counts = {}

# Opening our text file in read-only mode using the open() function
with open(r'1G.txt', 'r', encoding='latin-1') as file:
    # Reading the content of the file using the read() function and storing them in a new variable
    data = file.read()

    # Splitting the data into separate words using the split() function
    words = data.split()

    # Counting the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# Printing the count of each word
for word, count in word_counts.items():
    print(f"{word}: {count}")


