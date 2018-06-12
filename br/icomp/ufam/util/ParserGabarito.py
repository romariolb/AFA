#!/usr/bin/python3
import sys


def parseLog(str_file):
    gabList = []
    f_input = open(str_file, "r")
    count = 0
    for line in f_input:
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

    f_input.close()
    # print("Arquivo criado: ", "out" + str_file)
    return gabList


# print(sys.argv[1],sys.argv[2])
if len(sys.argv) == 2:  # and (os.path.isfile('./' + sys.argv[1])):
    f_name = sys.argv[1]
    parseLog(f_name)
