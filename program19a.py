# Program 19 Write Files
writeFile = open("log.txt", "w") #to clear change a to w and press enter to enter nothing
toLog = input("What is it that you people want me to write?")
writeFile.write(toLog)
writeFile.close()

writeFile = open("log.txt", "r")
print(writeFile.read())
writeFile.close()