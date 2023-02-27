# Program 18: Read Command
workfile = open('jackets.txt', "r")
workFileContents = workfile.read()
print(workFileContents)
workfile.close()
print("File has been closed")

# Readline Command
workFile = open('jackets.txt', "r")
workFileFirstLine = workFile.readline()
print(workFileFirstLine)
workFileSecondLine = workFile.readline()
print(workFileSecondLine)
workFile.close()
print("File has been closed")