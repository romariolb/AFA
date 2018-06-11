#!/usr/bin/python3
import sys


def parseLog(strfile):
    gabList = []
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
        gabList.append([out, t])
        # print(out,t)

    finput.close()
    print("Arquivo criado: ", "out" + strfile)
    return gabList


# print(sys.argv[1],sys.argv[2])
if len(sys.argv) == 2: # and (os.path.isfile('./' + sys.argv[1])):
    fname = sys.argv[1]
    parseLog(fname)
