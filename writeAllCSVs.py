import sys,io,glob

for arg in sys.argv[1:]:
    for files in glob.glob(arg):
        with open(files, "r") as file:
            line = file.readline()
            while line != '':
                lineList = line.split(',')
                with open(lineList[0], "r+b") as writeFile:
                          writeFile.seek(int(lineList[1]))
                          writeFile.write(bytes.fromhex(lineList[2]))
                line=file.readline()

# call as python writeAllCSVs.py *.csv