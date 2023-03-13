import sys
from fileparser import removecomments
from tokenizer import tokenize
from Compiler import CompilationEngine
from pathlib import Path
from Generator import Generator
import os

inputfolder = sys.argv[1]
inputpath = Path(inputfolder)
file_list = [str(pp) for pp in inputpath.glob("**/*.jack")]
for file in file_list:
    nameoffile = os.path.basename(file)[:-5]
    cleanlines = removecomments(file)
    tokens = tokenize(cleanlines)
    compiled = CompilationEngine(tokens)
    code = Generator(compiled)

    output = inputfolder+"/"+nameoffile + ".vm"
    with open(output, 'w') as file:
        file.writelines(code)
