#!/usr/bin/python

import sys
def printusage():
    usage = ""
    usage += "./b2d.py [option] [string]\n\n"
    usage += "Options: \n"
    usage += "  -b ; convert binary to decimal\n"
    usage += "  -d ; convert decimal to binary\n"
    usage += "  -l ; convert multiple values seperated by commas\n"
    usage += "  -8 ; outputs binary with leading zeros\n"
    usage += "Example: ./b2d -b 0010 -> returns 2\n"
    usage += "Example: ./b2d -d 24 -> returns 11000\n"
    usage += "Example: ./b2d.py -b -l 11110000,00111011  -> returns [240, 59]\n"
    usage += "Note: binary assumes the bit to the left is the lowest\n"
    usage += "  decimal will return highest bit to the right\n"

    print usage
def binary2decimal(binaryString):
    binaryString = binaryString[::-1]
    decimal = 0
    i = 0 
    while i < len(binaryString):
        if int(binaryString[i]) == 1:
            decimal += 2**i
        i+=1
    return decimal
def decimal2binary(decimalString):
    #This is going to be inefficient due to my small brain
    decimal = int(decimalString)
    binaryString = ""
    highestPower = 0
    while 2**highestPower< decimal:
        highestPower+=1
    highestPower -= 1

    while highestPower >= 0:
        if decimal >= 2**highestPower:
            binaryString += "1"
            decimal = decimal - 2**highestPower
        else:
           binaryString += "0"
           
        
        highestPower -=1
    if "-8" in sys.argv:
        while len(binaryString) < 8:
            binaryString = "0" + binaryString
    return binaryString
def listModeLogic(stringData):
    strings = stringData.split(',')
def auto(data):
    
    if "-d" in sys.argv:
        output = decimal2binary(data)
    elif "-b" in sys.argv:
        output = binary2decimal(data)
    else:
        printusage()
        sys.exit()
    return output

if len(sys.argv) < 2 :
    printusage()
    sys.exit()

if "-l" in sys.argv:
    data = sys.argv[-1].split(",")
    output = []
    for i in data:
        output.append(auto(i))
    print(output)
else:
    print auto(sys.argv[-1])
