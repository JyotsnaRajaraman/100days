import sys
from fileparser import removecomments
from translator import translate
import os

# take foldername from user

directory = sys.argv[1]

# extract folder name for .asm file creation
directoryName = os.path.dirname(directory)
files = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a valid vm file
    if os.path.isfile(f) and f[-3:] == ".vm":
        files.append(f)
# set sp to 256
final = ["@256\nD=A\n@SP\nM=D\n"]
# call sys init
final += translate(["call Sys.init"])
for inputfile in files:
    nameoffile = (os.path.basename(inputfile))[:-3]
    # remove comments and whitespace
    cleanlines = removecomments(inputfile)
    # iterate through each line and translate
    final += translate(cleanlines, nameoffile)
    # write the new content to an .out file
outfile = directoryName + "/" + directoryName + ".asm"
with open(outfile, 'w') as file:
    file.writelines(final)
