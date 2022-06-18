# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Clear contents and write to file
# with open("my_file.txt", mode="w") as file:
#     file.write("New text for my file")

# Append Text in file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nAnother line of new text.")

# Add a file that does not already exist  -only works in write mode
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")
