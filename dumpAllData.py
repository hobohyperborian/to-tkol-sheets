import io,sys

# useage via powershell, cygwin, or command prompt:
#     python dumpAllData.py rom.gba > tableDump.txt 
#
# make sure filename is correct, python 3 is installed
# might work with python 2, i don't know
# replace rom.gba with name of your to tkol rom
# tableDump.txt can be any name.

with open(sys.argv[1], 'rb') as rom:
    def printData(addr, rows, reads, name):
        rom.seek(addr)
        tblList = []
        rowCntr = 0
        while rowCntr < rows:
            tblList.insert(rowCntr, bytearray(rom.read(reads)))
            rowCntr += 1
        rowCntr = 0
        print(name)
        for i in range(0, rows, 1):
            for j in range(0, reads, 1):
                # if printing ints, uncomment this one below
                # print(str(int(b)), end=' ')
                # if printing hex, uncomment this one below
                # print(hex(b)[2:].zfill(2), end=' ')
                # if printing hex for paste into spreadsheet, use this one below
                print('\'' + hex(tblList[i][j])[2:].zfill(2), end='\' ')
                # only use one at a time, comment all others
                # <--this hashtag is a comment
            rowCntr += 1
            print()
        print()

    def printDataTranspose(addr, rows, reads, name):
        rom.seek(addr)
        tblList = []
        rowCntr = 0
        while rowCntr < rows:
            tblList.insert(rowCntr, bytearray(rom.read(reads)))
            rowCntr += 1
        rowCntr = 0
        print(name)
        for i in range(0, reads, 1):
            for j in range(0, rows, 1):
                # if printing ints, uncomment this one below
                # print(str(int(b)), end=' ')
                # if printing hex, uncomment this one below
                # print(hex(b)[2:].zfill(2), end=' ')
                # if printing hex for paste into spreadsheet, use this one below
                print('\'' + hex(tblList[j][i])[2:].zfill(2), end='\' ')
                # only use one at a time, comment all others
                # <--this hashtag is a comment
            rowCntr += 1
            print()
        print()

    #printData(startingAddress, entries, byesPerEntry, name)
    printData(6400240, 127, 64, "Abilities " + str(6400240))
    printData(6372464, 81, 20, "Characters " + str(6372464))
    printDataTranspose(6378112, 84, 88, 'Classes ' + str(6378112))
    printData(7770416, 810, 32, "Formations " + str(7770416))
    printData(6385504, 192, 36, "Items " + str(6385504))
    printData(6431892, 10, 8, "Shops - Hirelings " + str(6431892))
    printData(6432132, 8, 1, "Shops - Deneb <3 " + str(6432132))
    printData(6431972, 40, 4, "Shops - Items " + str(6431972))
    printData(6432140, 35, 4, "Shops - Magic " + str(6432140))
    printData(6412448, 36, 3, "Treasures - Underground " + str(6412448))
    printData(6412556, 10, 8, "Treasures - Quests " + str(6412556))
    printData(6412636, 8, 8, "Treasures - Versus " + str(6412636))

# copy and paste this for all tables you want to print.
# don't forget to edit this print statement, comment it out, or delete it.
# printData(startingAddress, entries, byesPerEntry, name)
# startingAddress is starting address in decimal (base 10)
# others should be self explanatory.

