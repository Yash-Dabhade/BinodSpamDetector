# Binod detector and Cleaner
import os


def DetectBinod(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
    if "binod" in filecontent.lower():
        return True
    else:
        return False


count = 0
affectedfiles = []
print("Welcome to the Binod Spam Detector !!!")
print("PLEASE OPEN THIS FILE IN THE FOLDER TO BE SCAN ***")
print("Enter Y to detect:")
ch = input()
files = os.listdir()
files.remove("BinodDetector.py")
if ch == 'y' or ch == 'Y':
    print("----Detecting Binod Spam in The files----\n\t\t^^^^FIles Scannned^^^^")
    for item in files:
        if os.path.isfile(item):
            print(item)
            flag = DetectBinod(item)
            if flag:
                count += 1
                affectedfiles.append(item)
print()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()
print("<<<<< Summary >>>>>")
print(f"Total Files Affected ::{count}")
print("Files affected are ::")
for i in affectedfiles:
    print(i)

print("Enter Y To delete all the spam files or N to exit ::")
dch = input()
if dch == 'Y' or dch == 'y':
    for file in affectedfiles:
        os.remove(file)
    print("Files Deleted Successfully !!!")
input()
