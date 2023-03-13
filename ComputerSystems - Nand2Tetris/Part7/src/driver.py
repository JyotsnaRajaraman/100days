import sys
from fileparser import removecomments
from translator import translate
import os

# take filename from user
inputfile = sys.argv[1]
# isolate filename
nameoffile = (os.path.basename(inputfile))[:-3]
# remove comments and whitespace
cleanlines = removecomments(inputfile)
# iterate through each line and translate
final = translate(cleanlines, nameoffile)
# write the new content to an .out file
outfile = nameoffile + ".asm"
with open(outfile, 'w') as file:
    file.writelines(final)
