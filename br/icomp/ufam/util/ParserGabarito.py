#!/usr/bin/python3
import sys


def parseLog(str_file):
    gabList = []
    f_input = open(str_file, "r")
    count = 0
    for line in f_input:
        count += 1
        q, ra, rb, rc, rd, re, d1, d2, d3, t = line.replace("\n", "").split(" ")
        out1 = "Q" + q
        if ra == '4':
            out2 = out1 + "A"
        elif rb == '4':
            out2 = out1 + "B"
        elif rc == '4':
            out2 = out1 + "C"
        elif rd == '4':
            out2 = out1 + "D"
        elif re == '4':
            out2 = out1 + "E"
        else:
            out2 = out1 + "X"
        gabList.append([out2, int(t), out1])
        # print(out,t)

    f_input.close()
    # print("Arquivo criado: ", "out" + str_file)
    return gabList


# print(sys.argv[1],sys.argv[2])
if len(sys.argv) == 2:  # and (os.path.isfile('./' + sys.argv[1])):
    f_name = sys.argv[1]
    parseLog(f_name)
