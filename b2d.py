#!/usr/bin/python

import sys

def printusage():
    usage = ""
    usage += "./b2d.py [option] [string]\n\n"
    usage += "Options: \n"
    usage += "  -b ; convert binary to decimal\n"
    usage += "  -d ; convert decimal to binary\n"
    usage += "Example: ./b2d -b 0010 -> returns 2\n"
    usage += "Example: ./b2d -d 24 -> returns 11000\n"
    usage += "Note: binary assumes the bit to the left is the lowest\n"
    usage += "  decimal will return highest bit to the right\n"

    print usage
    sys.exit()
def binary2decimal(binaryString):
    binaryString = binaryString[::-1]
    decimal = 0
    i = 0 
    while i < len(binaryString):
        if int(binaryString[i]) == 1:
            decimal += 2**i
        i+=1
    print decimal
    sys.exit()
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
            print (decimal,2**highestPower)
            decimal = decimal - 2**highestPower
            print decimal
        else:
           binaryString += "0"
           
        
        highestPower -=1

    print binaryString
    sys.exit()
if len(sys.argv) < 2 :
    printusage()
if sys.argv[1] == "-d":
    decimal2binary(sys.argv[2])
if sys.argv[1] == "-b":
    binary2decimal(sys.argv[2])
printusage()
