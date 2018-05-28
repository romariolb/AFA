""" This program implements a parser and data structure for Petri net files.

This program implements an XML parser and a python data structure for
Petri nets/PNML created with VipTool or MoPeBs.
"""

import sys  # argv for test file path
import csv
from br.icomp.ufam.petrinet.PNet import PNet
from br.icomp.ufam.petrinet.PNetPlace import PNetPlace
from br.icomp.ufam.petrinet.PNetTransition import PNetTransition
from br.icomp.ufam.petrinet.PNetArc import PNetArc


class ParsePetriNet:
    """ This class represents a Petri net.

    This class represents a Petri net. A Petri net consists of
    a set of labelled labelled transitions, labelled places and
    arcs from places to transitions or transitions to places.

    net.edges: List of all edges of this Petri net
    net.transitions: Map of (id, transition) of all transisions of this Petri net
    net.places: Map of (id, place) of all places of this Petri net
    """

    def __init__(self):
        self.aluno = None
        self.net = ''

    def __str__(self):

        text = '--- Net:\nTypes:\n'

        text += '\nTransitions:\n'
        for transition in self.net.listT:
            text += str(transition) + '\n'
        text += '\nPlaces:\n'
        for place in self.net.listP:
            text += str(place) + '\n'
        text += '\nArcos:\n'
        for edge in self.net.listA:
            text += str(edge) + '\n'
        text += '\nMarcação Inicial\n'

        return text

    def parse_csv_file(self, file):

        self.net = PNet()

        placeS = PNetPlace('S', None, None, None, None)
        placeS.count += 1
        self.net.addPlace(placeS)
        placeSS = PNetPlace('SS', None, None, None, None)
        placeSS.count += 1
        self.net.addPlace(placeSS)

        transition0 = PNetTransition(0)
        self.net.addTransition(transition0)

        arcS = PNetArc(self.net.listP[placeS.node.id], self.net.listT[transition0.node.id],
                       self.net.listP[placeS.node.id].count, self.net)
        self.net.addArc(arcS)

        with open(file, 'r') as log:
            t_max = sum(1 for row in log)
            t_max = t_max * 2

            """
            Criação dos objetos de transição.
            O numero total de transições é o dobro de linhas do arquivo
            """
            for t in range(1, t_max + 1):
                transition1 = PNetTransition(t)
                self.net.addTransition(transition1)

        log.close()

        with open(file, 'r') as log:

            last = self.net.listT[transition0.node.id]

            reader = csv.reader(log, delimiter=';')

            for linha in reader:
                """
                Leitura dos componentes do .csv para atribuição aos objetos
                """
                self.aluno = linha[2]
                TEMPO = linha[3]
                foco = linha[6]
                tmp = foco.split(':')
                QUESTAO = str(tmp[0] + tmp[1])
                DIFC = str(tmp[2])
                RESPOSTA = QUESTAO + str(tmp[4])
                tmp2 = tmp[3].split('-')
                DISCIPLINA = str(tmp2[0])
                TOPICO = str(tmp2[1])

                """
                criação dos objetos de lugares
                
                faz uma verificação se o lugar ja existe no map de lugares
                se existir ele incrementa o contador do lugar com +1
                senão, ele insere o lugar novo e inicia o contador com 1
                """

                placeQ = PNetPlace(QUESTAO, DISCIPLINA, TOPICO, DIFC, TEMPO)

                if placeQ.node.id in self.net.listP:
                    self.net.listP[placeQ.node.id].count += 1
                else:
                    self.net.addPlace(placeQ)
                    self.net.listP[placeQ.node.id].count += 1

                placeR = PNetPlace(RESPOSTA, None, None, None, TEMPO)

                if placeR.node.id in self.net.listP:
                    self.net.listP[placeR.node.id].count += 1
                else:
                    self.net.addPlace(placeR)
                    self.net.listP[placeR.node.id].count += 1

                """
                Criação dos objetos de Arcos.
                """

                arc1 = PNetArc(last, self.net.listP[placeQ.node.id], self.net.listP[placeQ.node.id].count, self.net)
                arc2 = PNetArc(self.net.listP[placeQ.node.id], self.net.listT[last.node.id + 1],
                               self.net.listP[placeQ.node.id].count, self.net)
                arc3 = PNetArc(self.net.listT[last.node.id + 1], self.net.listP[placeR.node.id],
                               self.net.listP[placeR.node.id].count, self.net)
                arc4 = PNetArc(self.net.listP[placeR.node.id], self.net.listT[last.node.id + 2],
                               self.net.listP[placeR.node.id].count, self.net)

                self.net.addArc(arc1)
                self.net.addArc(arc2)
                self.net.addArc(arc3)
                self.net.addArc(arc4)

                last = self.net.listT[last.node.id + 2]

            arcSS = PNetArc(last, self.net.listP[placeSS.node.id], self.net.listP[placeSS.node.id].count,
                            self.net)
            self.net.addArc(arcSS)

            self.net.id = self.aluno

        log.close()

        return self.net
