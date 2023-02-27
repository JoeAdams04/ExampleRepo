#Program 21: Delete Files
import os
if os.path.isfile('log_old.txt'):
    os.remove('log_old.txt')
    print("The log_old file has been removed!")
else:
    print("There was no log_old file to remove!")
