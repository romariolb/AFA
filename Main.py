import sys  # argv for test file path
from collections import OrderedDict

from br.icomp.ufam.metrics.Deviation import Deviation
from br.icomp.ufam.parse.ParsePetriNet import ParsePetriNet
from br.icomp.ufam.util.Matrix import Matrix
from br.icomp.ufam.util.PNetExe import PNetExe
from br.icomp.ufam.util.ParserGabarito import parseLog
from br.icomp.ufam.metrics.Score import Score
from br.icomp.ufam.metrics.Doubt import Doubt

# TESTE DE PARSER
log = sys.argv[1]
gab = sys.argv[2]
n_q = sys.argv[3]
answers_list = parseLog(str(gab))
net = ParsePetriNet(str(gab)).parse_csv_file(str(log), answers_list)

print(net)

matrix = Matrix(net)
matrix.setMatrixI()
matrix.setMatrixO()
matrix.setMatrixD()
print(matrix)

exe = PNetExe(matrix, int(n_q))
exe.initMark()
print(exe)
exe.calculation()
print(exe)

score = Score(exe.marking, int(n_q), net)
score.calculus()
print(score)

doubt = Doubt(score.corrects, score.incorrect, 3)
doubt.doubtLevel()
print(doubt)

dev = Deviation(exe.marking, int(n_q), net, score)
dev.listIncorrects()
dev.mapQuest()
dev.calculus()
print(dev)


"""def returnArc(src, tgt, net):
    for arc in net.listA:

        if src[0] == arc.source[0] and tgt[0] == arc.target[0]:
            return arc


def exportGraph(net, fpath):
    outFile = fpath.split(".")[0]

    fobj = open(outFile + ".dot", "w")

    # DOT FILE HEADER

    fobj.write("digraph G { rankdir=LR; splines=polyline;\n")

    fobj.write(
        "node[style=filled; fontsize=10; fontname=Arial; fontcolor=black; fillcolor=white; colorscheme=bugn9];\n")

    # SUBTITLE CLUSTERS

    fobj.write("subgraph cluster_0{subgraph cluster_1{ label=\"Legenda de Duvida\"\n")

    for i in range(1, 6):

        if i >= 3:
            fobj.write("\"Nivel " + str(i) + "\"[colorscheme=reds5; fillcolor=" + str(i) + "; fontcolor=white;]\n")

        else:
            fobj.write("\"Nivel " + str(i) + "\"[colorscheme=reds5; fillcolor=" + str(i) + ";]\n")

    fobj.write("}\nsubgraph cluster_2{ label=\"Legenda de Desvio\"\n")

    for i in range(1, 6):

        if i > 3:
            fobj.write("\"Desvio " + str(i) + "\"[fillcolor=" + str(i + 2) + "; fontcolor=white;];\n")

        else:
            fobj.write("\"Desvio " + str(i) + "\"[fillcolor=" + str(i + 2) + ";];\n")

    fobj.write("}}\n")

    areasRank = OrderedDict()

    # GET THE NUMBER OF VISITS FROM THE MOST VISITED PLACE

    maxCount = 0

    for i in net.listP:

        if i[1].count > maxCount: maxCount = i[1].count

    # THE REAL STUFF!

    for i in net.listP:

        nodeatts = "fillcolor=white;"

        # GROUPING QUESTIONS BY AREA

        if i[1].discipline:

            area = int(i[1].discipline)

            if area not in areasRank.keys():
                areasRank[area] = "{rank=same; "

            areasRank[area] = areasRank[area] + "\"" + i[1].name + "\"; "  # COLLECT QUESTIONS

            # QUESTION COLORS (CONFUSION METRIC)

            weight = (5 * i[1].count) // maxCount

            nodeatts = "colorscheme=\"reds5\"; fillcolor=" + str(weight) + "; "

            if ((weight) > 2): nodeatts += "fontcolor=white;";



        else:

            # HANDLE THE INITIAL(S) AND FINAL(SS) PLACES

            if i[1].name.upper() == "S" or i[1].name.upper() == "SS":

                nodeatts = "fillcolor=black; shape=point; width=0.3; xlabel=\"" + i[1].name + "\";"

                fobj.write("\"" + i[1].name + "\"[" + nodeatts + "];")

            else:

                # CHECK IF IS ANSWER AND PAINT(DEVIATION METRIC)

                if i[1].name[-1].isalpha():

                    nodeatts = "fillcolor=" + str(i[1].desvio + 2) + "; "

                    if ((i[1].desvio + 2) >= 5): nodeatts += "fontcolor=white;";

        # PRINT IF IS A QUESTION OR ANSWER

        if i[1].name[-1].upper() != "V" and i[1].name.upper() != "S" and i[1].name.upper() != "SS":
            fobj.write("\"" + i[1].name + "\"[" + nodeatts + "]; ")  # , end='')

    # Transactions List

    for i in net.listT: fobj.write(
        "\"" + i[1].name + "\"[fillcolor=black; shape=box; label=\"\"; width=0.01; fontsize=9; xlabel=\"" + i[
            1].name + "\"]; ")  # ,end='')

    # Places List

    for i in areasRank.keys(): fobj.write(areasRank[i] + "}")

    # Arcs List

    for i in net.listA:

        arcInfo = returnArc(i.source, i.target, net)

        lbArc = "[label=\"" + str(arcInfo.inscription) + "\";];"

        if arcInfo.inscription == 1: lbArc = str("")

        fobj.write("\"" + i.find_source().name + "\"->\"" + i.find_target().name + "\"" + lbArc + " ")

    fobj.write("}")

    fobj.close()

    print(
        "Export Done! Create an image with this command(demands Graphviz): dot -Tjpg " + outFile + ".dot -o " + outFile + ".jpg")


exportGraph(net, log)"""
