#!/usr/bin/python3 
import sys
import os
import datetime
import operator
import random
from collections import OrderedDict
from math import *
#from numpy import *
from subprocess import *


def parseLog(strfile):
    foutput = open("./out", "w")
    finput = open(strfile, "r")
    count = 0
    for line in finput:
        count += 1
        out = "Q" + str(count)
        q, ra, rb, rc, rd, re, d1, d2, d3, t = line.replace("\n", "").split(" ")
        if int(ra) == 5:
            out = out + "A"
        elif int(rb) == 5:
            out = out + "B"
        elif int(rc) == 5:
            out = out + "C"
        elif int(rd) == 5:
            out = out + "D"
        elif int(re) == 5:
            out = out + "E"
        else:
            out = out + "X"
        foutput.write(out + "\t" + t + "\n")
        # print(out,t)

    foutput.close()
    finput.close()
    print("Arquivo criado: ", "out" + strfile)


# print(sys.argv[1],sys.argv[2])
if len(sys.argv) == 2: # and (os.path.isfile('./' + sys.argv[1])):
    fname = sys.argv[1]
    parseLog(fname)
