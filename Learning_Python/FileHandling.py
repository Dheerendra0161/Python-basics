# File Handling in  python
# open a file using the open() function.
'''
Modes:
'r': Read mode (default). Opens a file for reading. Raises an error if the file does not exist.
'w': Write mode. Opens a file for writing. Creates a new file if it does not exist, truncates the file if it exists.
'a': Append mode. Opens a file for appending. Creates a new file if it does not exist.
'r+': Read/write mode. Opens a file for both reading and writing.
'b': Binary mode. Add 'b' to a mode to open a file in binary mode, e.g., 'rb' or 'wb'.
'''

# Opening a file in write mode
file = open("fileText.txt", "w")  # File with name "fileText" will be created in project

# Writing to a File:   write() method. It writes a string to the file.
file.write("Hello, world!\n")
file.write(
    "This is a new line.\nDheerendra is learning python as programming language for selenium automation\nhttps://github.com/Dheerendra0161/new-Demo-rep"
    "\nhttps://chat.openai.com/c/42c6417c-3911-4736-8ae5-22d80e51d29a")
file.close()  # Always remember to close the file using file.close() after you have finished writing to it.

# file.write(str)  :. If the file is opened in write ("w") or append ("a") mode, it will write the string to the file. If the file does not exist, it will be created.
with open("outputFile.txt", "w") as file:
    file.write("Hello, File!")

# Reading from a File:read() method. It reads the entire file contents.
file = open("fileText.txt", "r")  # r+ mode is used to read/write
content = file.read()
print(content)
file.close()

# Appending to a File:You can append to an existing file using the 'a' mode.
file = open("fileText.txt",
            "a")  # "a" mode is used when you want to append data to a file without erasing the existing content.
# If the file does not exist, it will be created. If it does exist, the file pointer will be positioned at the end of the file.
file.write("\nThis line is appended.")
file.close()

'''
Example Output (fileText.txt):
If "example.txt" initially contains:
"This is the initial content of the file."

After running the provided code, the file "example.txt" will contain:
This is the initial content of the file.
This line is appended.
'''

# Reading a file with error handling using 'with' statement

# One of the main advantages is that with keyword automatically closes the file when the block inside with is exited.
# You don't need to explicitly call file.close() to close the file.
# This ensures that resources are released and the file is properly closed, even if an error occurs within the block.
try:
    with open('file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")

# file.read(size=-1)   : optional size parameter to indicate the number of bytes to read. If no size is specified, it will read the entire file.
with open("fileText.txt",
          "r") as file:  # with statement ensures that files are properly closed after their suite finishes, even if an exception is raised.
    content = file.read()
    print(content)

# file.readline() method :reads a single line from the file. If called again, it will read the next line, and so on.
with open('fileText.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print("Line 1:", line1)
    print("Line 2:", line2)

# To read a specific value from the file.
urlToFind = "https://github.com/Dheerendra0161/new-Demo-rep"
with open("fileText.txt", 'r') as file:
    for line in file:
        if urlToFind in line:
            url = line.strip()
            break
if url:
    print("URL found:", url)
else:
    print("URL not found in the file.")

# Other way to read specific string in file
urlToFind = "https://chat.openai.com/c/42c6417c-3911-4736"
with open("fileText.txt", 'r') as file:
    url = next((line.strip() for line in file if urlToFind in line), None)  # retrieves the next item from the iterator.
if url is not None:
    print("URL found:", url[0:25])  # To get only https://chat.openai.com/c/
else:
    print("URL not found in the file.")
