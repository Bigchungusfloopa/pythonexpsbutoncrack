import string

# Step 1: Get filename from user
filename = input("Enter the filename: ")

# Step 2: Create and write content to the file
with open(filename, "w") as obj:
    obj.write("hi these file contains three four and five length string words !!!")

# Step 3: Take user input for word lengths
n = int(input("Enter the number of elements in lengths: "))
lengths = [int(input(f"Enter length {i+1}: ")) for i in range(n)]

# Step 4: Read file and extract words
with open(filename, 'r') as file:
    text = file.read()
    words = text.translate(str.maketrans('', '', string.punctuation)).split()

# Step 5: Filter words based on specified lengths
for length in lengths:
    filtered_words = [word for word in words if len(word) == length]
    print(f'Words of length {length}:', filtered_words)
