# import sys  # argv for test file path
import csv
import os
import sys
from collections import OrderedDict

from br.icomp.ufam.metrics.Confusion import Confusion
from br.icomp.ufam.metrics.Deviation import Deviation
from br.icomp.ufam.metrics.Doubt import Doubt
from br.icomp.ufam.metrics.Score import Score
from br.icomp.ufam.metrics.WeightedScore import WeightedScore
from br.icomp.ufam.parse.ParsePetriNet import ParsePetriNet, returnArc
from br.icomp.ufam.util.BuildFiles import BuildFiles
from br.icomp.ufam.util.Matrix import Matrix
from br.icomp.ufam.util.ParserGabarito import parseLog
from br.icomp.ufam.util.PNetExe import PNetExe

# python Main.py Support/Files/logs-2018-2/3934.1D/SERVICE_log_3934.1D.csv Support/Files/logs-2018-2/3934.1D/gabaritoPCompreensao_3934.1D.txt 44 4 day class

def exportGraph(net, fpath, student):
    outFile = fpath.split(".")[0]

    fobj = open(student + ".dot", "w")

    # DOT FILE HEADER

    fobj.write("digraph G { rankdir=LR; splines=polyline;\n")

    fobj.write(
        "node[style=filled; fontsize=10; fontname=Arial; fontcolor=black; fillcolor=white; colorscheme=bugn9];\n")

    # SUBTITLE CLUSTERS

    """fobj.write("subgraph cluster_0{subgraph cluster_1{ label=\"Legenda de Duvida\"\n")

    for i in range(1, 6):

        if i >= 3:
            fobj.write("\"Nivel " + str(i) + "\"[colorscheme=reds5; fillcolor=" + str(1) + "; fontcolor=white;]\n")
        elif i == 2:
            fobj.write("\"Nivel " + str(i) + "\"[colorscheme=reds5; fillcolor=" + str(1) + ";]\n")
        elif i == 1:
            fobj.write("\"Nivel " + str(i) + "\"[colorscheme=reds5; fillcolor=" + str(1) + ";]\n")

    fobj.write("}\nsubgraph cluster_2{ label=\"Legenda de Desvio\"\n")

    for i in range(1, 6):

        if i > 3:
            fobj.write("\"Desvio " + str(i) + "\"[fillcolor=" + str(i + 2) + "; fontcolor=white;];\n")

        else:
            fobj.write("\"Desvio " + str(i) + "\"[fillcolor=" + str(i + 2) + ";];\n")

    fobj.write("}}\n")"""

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

            nodeatts = "colorscheme=\"reds5\"; fillcolor=white; "

            if ((weight) > 2): nodeatts += "fontcolor=black;"

        else:

            # HANDLE THE INITIAL(S) AND FINAL(SS) PLACES

            if i[1].name.upper() == "S" or i[1].name.upper() == "SS":

                nodeatts = "fillcolor=black; shape=point; width=0.3; xlabel=\"" + i[1].name + "\";"

                fobj.write("\"" + i[1].name + "\"[" + nodeatts + "];")

            else:

                # CHECK IF IS ANSWER AND PAINT(DEVIATION METRIC)

                if i[1].name[-1].isalpha():

                    nodeatts = "fillcolor=" + str(i[1].deviation + 2) + "; "

                    if ((i[1].deviation + 2) >= 5): nodeatts += "fontcolor=white;"

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

    os.system("dot -Tjpg " + student + ".dot -o " + student + ".jpg")

    # print(
    #    "Export Done! Create an image with this command(demands Graphviz): dot -Tjpg " + student + ".dot -o " + student + ".jpg")

day = str(sys.argv[5])  # dia da avaliacao
_class = str(sys.argv[6]) # numero da turma
full_log = BuildFiles(sys.argv[1], day, _class)
listStudents = full_log.create_list()
"""print('teste de log \n')
print(full_log)
print('\n')"""
full_log.create_files()
full_log.fill_files()

gab = sys.argv[2]  # gabarito
n_q = int(sys.argv[3])  # numero de questoes
n_f = int(sys.argv[4])  # numero de questoes faltantes
answers_list = parseLog(str(gab))

# for a in answers_list:
#    print(a)

export = csv.writer(open("Report-" + _class + '-' + day + ".csv", "wb"))
class_correct = []
class_questions = []

confusion = Confusion()

print('Carregando...')

for student in listStudents:
    file_student = './logs/' + _class + '/' + day + '/' + str(student)
    file = full_log.findFiles(file_student, '.csv')
    # print(file)
    net = ParsePetriNet(str(gab)).parse_csv_file(str(file[0]), answers_list)
    # print(str(student))
    # print(net.getFOut())
    matrix = Matrix(net)
    matrix.setMatrixI()
    matrix.setMatrixO()
    matrix.setMatrixD()
    # print(matrix)
    exe = PNetExe(matrix, n_q, n_f)
    exe.initMark()
    exe.calculation()
    # Score
    score = Score(exe.marking, int(n_q), net, n_f, answers_list)
    score.calculus()
    correct = score.getCorrects()
    confusion.num_corrects(correct) # para a metrica de confusao
    incorrect = score.getIncorrect()
    confusion.count_marks_questions(incorrect)
    # w_score
    w_score = WeightedScore(exe.marking, n_q, net, n_f, correct, incorrect)
    w_score.listIncorrects()
    w_score.mapQuest()
    w_score.calculus()
    w_s = w_score.getScore()
    # desvio
    dev = Deviation(exe.marking, int(n_q), net, score, n_f, w_s, incorrect)
    dev.listIncorrects()
    dev.mapQuest()
    dev.calculus()
    #duvida
    doubt = Doubt(score.corrects, score.incorrect, 3)
    doubt.doubtLevel()

    """print(net)
    print('\n==PONTUACAO TRADICIONAL==\n')
    print(score)
    print('\n==NOTA PONDERADA==\n')
    print(w_score)
    print('\n==PERCENTUAL DE DESVIO==\n')
    print(dev)
    print('\n==NIVEL DE DUVIDA==\n')
    print(doubt)

        FORMAT REPORT.CSV
        id_student, score, weight_score, deviation_level, most_correct_question_doubt - value : most_incorrect_question_doubt - value
    """
    if os.path.getsize(file_student + '/' + str(student) + '.csv') > 0:
        if not doubt.orderedCorrect:
            # export.writerow([str(student), str(score.score), str(w_score.score), str(dev.scoreD), 'Qx' + '-' + '0' + ':' + str(doubt.orderedIncorrect[0][0]) + '-' + str(doubt.orderedIncorrect[0][2])])
            pass
        elif not doubt.orderedIncorrect:
            # export.writerow([str(student), str(score.score), str(w_score.score), str(dev.scoreD), str(doubt.orderedCorrect[0][0]) + '-' + str(doubt.orderedCorrect[0][2]) + ':' + 'Qx' + '-' + '0'])
            pass
        elif not doubt.orderedCorrect and not doubt.orderedIncorrect:
            # export.writerow([str(student), str(score.score), str(w_score.score), str(dev.scoreD), 'Qx' + '-' + '0' + ':' + 'Qx' + '-' + '0'])
            pass
        else:
            export.writerow([str(student), str(score.score), str(w_score.score), str(dev.scoreD), str(doubt.orderedCorrect[0][0]) + '-' + str(doubt.orderedCorrect[0][2]) + ':' + str(doubt.orderedIncorrect[0][0]) + '-' + str(doubt.orderedIncorrect[0][2])])
    else:
        pass

    exportGraph(net, file_student + '/' + str(student) + '.csv', file_student + '/' + str(student))
    print('...')

#confusao
confusion.total_marks_corrects()
confusion.confusionLevel()
print(confusion)   

print('\n Report exported \n')



"""files = full_log.findFiles('./logs', '.csv')
for path in files:
    log = path  # log
    net = ParsePetriNet(str(gab)).parse_csv_file(str(log), answers_list)
    print(net)
    matrix = Matrix(net)
    matrix.setMatrixI()
    matrix.setMatrixO()
    matrix.setMatrixD()
    # print(matrix)
    exe = PNetExe(matrix, n_q, n_f)
    exe.initMark()
    exe.calculation()
    print('\n=================PONTUACAO TRADICIONAL===================\n')

    score = Score(exe.marking, int(n_q), net, n_f, answers_list)
    score.calculus()
    print(score)
    correct = score.getCorrects()
    incorrect = score.getIncorrect()

    print('\n=================NOTA PONDERADA===================\n')

    w_score = WeightedScore(exe.marking, n_q, net, n_f, correct, incorrect)
    w_score.listIncorrects()
    w_score.mapQuest()
    w_score.calculus()
    print(w_score)
    w_s = w_score.getScore()

    print('\n=================PERCENTUAL DE DESVIO===================\n')

    dev = Deviation(exe.marking, int(n_q), net, score, n_f, w_s, incorrect)
    dev.listIncorrects()
    dev.mapQuest()
    dev.calculus()
    print(dev)

    print('\n=================NIVEL DE DUVIDA===================\n')

    doubt = Doubt(score.corrects, score.incorrect, 3)
    doubt.doubtLevel()
    print(doubt)"""

# TESTE DE PARSER
"""

print('\n=================NIVEL DE DUVIDA===================\n')"""

"""doubt = Doubt(score.corrects, score.incorrect, 3)
doubt.doubtLevel()
print(doubt)

print('\n=================NIVEL DE CONFUSAO===================\n')
"""
"""confusion = Confusion(score.corrects, score.incorrect)
confusion.confusionLevel()
confusion.calculus()
print(confusion)"""

"""def returnArc(src, tgt, net):
    for arc in net.listA:

        if src[0] == arc.source[0] and tgt[0] == arc.target[0]:
            return arc
"""



