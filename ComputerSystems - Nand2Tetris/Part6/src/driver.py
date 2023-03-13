import sys
from fileparser import removecomments
from translator import translate, removelabels

# take filename from user
inputfile = "Project6WetTest.asm"
# sys.argv[1]
# remove comments and whitespace
cleanlines = removecomments(inputfile)
# iterate through each line and translate
pass1 = []
linecount = 0

labelfree = removelabels(cleanlines)
final = translate(labelfree)

# write the new content to an .out file
outfile = inputfile[:-4] + ".hack"
with open(outfile, 'w') as file:
    file.writelines(final)
