import sys
from fileparser import removecomments
from tokenizer import tokenize
from Compiler import CompilationEngine
from pathlib import Path
import os

inputfolder = sys.argv[1]
inputpath = Path(inputfolder)
file_list = [str(pp) for pp in inputpath.glob("**/*.jack")]
for file in file_list:
    nameoffile = os.path.basename(file)[:-5]

    cleanlines = removecomments(file)

    outputT = inputfolder + "/" + nameoffile + "T.xml"
    tokens = tokenize(cleanlines)
    with open(outputT, 'w') as file:
        file.writelines(tokens)

    output = inputfolder+"/"+nameoffile + ".xml"

    compiled = CompilationEngine(tokens)

    with open(output, 'w') as file:
        file.writelines(compiled)
