def removecomments(userinput):
    # open the file
    with open(userinput, "r") as file1:
        # removing single line comments
        lines = file1.readlines()
        contents = list(map(lambda x: x[:x.find("//")] + "\n", lines[:-1]))
        # remove all trailing tabspaces
        contents = list(map(lambda x: x[:x.find("\t")] + "\n", contents))
        # for final line (handling case when no /n at the EOF)
        finalline = lines[-1]
        if finalline.find("//") == -1:
            contents = contents + [finalline]
        else:
            contents = contents + [finalline[:finalline.find("//")]]
        # removing multiline comments
        i = 0
        while i < (len(contents)):
            # find where the comment starts
            startofcom = contents[i].find("/*")
            if startofcom != -1:
                # if there is a comment on the line, see if it ends on the same line
                endofcom = contents[i].find("*/")
                while endofcom == -1:
                    # remove the commented part
                    contents[i] = contents[i].replace(
                        contents[i][startofcom:endofcom], '')
                    i = i + 1
                    endofcom = contents[i].find("*/")
                contents[i] = contents[i].replace(
                    contents[i][startofcom:endofcom+2], '')
            i = i + 1
        # removing all leading whitespaces
        cleanlines = [x.replace(" ", "") for x in contents]
        cleanlines = [i for i in cleanlines if i != "\n"]
        return [i for i in cleanlines if i]
