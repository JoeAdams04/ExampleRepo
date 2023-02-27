# Program 19b: Write Files
file1 = open("myfile.txt", "w")
L = ["This is Ohio \n", "This is Tennessee \n", "This is Kentucky"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a") # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w") # Write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of ReadLines after writing")
print(file1.read())
print()
print(file1.close())
