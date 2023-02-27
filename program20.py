#Program 20
import os
if os.path.isfile('log.txt'):
    writeFile = open('log.txt', 'a')
else:
    writeFile = open('log.txt', 'w')

toLog = input("What would you like to write to the log?")
writeFile.write("\n" + toLog)
writeFile.close()