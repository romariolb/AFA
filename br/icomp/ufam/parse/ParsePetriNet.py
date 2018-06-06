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
        self.net = 'Teste'
        self.tupla1, self.tupla2 = (0, 0)
        #print('criou obj NET {}'.format(self.net))

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
        text += '\nMarcacao Inicial\n'

        return text

    def parse_csv_file(self, file):
        #print('entrou no metodo parse_csv')

        self.net = PNet()

        #print('instaciou obj NET')

        placeS = PNetPlace('S', None, None, None, None)
        placeS.count += 1
        tuplaS = ('S', placeS)
        self.net.addPlace(tuplaS)

        #print('criou o 1 lugar S')

        transition0 = PNetTransition(0)
        tupla0 = (0, transition0)
        self.net.addTransition(tupla0)

        #print('criou a primeira transicao')

        arcS = PNetArc(tuplaS, tupla0,
                       tuplaS[1].count, self.net)
        self.net.addArc(arcS)

        #print('criou o 1 arco')

        with open(file, 'r') as log:
            t_max = sum(1 for row in log)
            t_max = t_max * 2

            """
            Criacao dos objetos de transicao.
            O numero total de transicoes eh o dobro de linhas do arquivo
            """
            for t in range(1, t_max + 1):
                transition1 = (t, PNetTransition(t))
                self.net.addTransition(transition1)
            #print('criou as transicoes')

        log.close()

        with open(file, 'r') as log:

            last = self.net.listT[0]

            reader = csv.reader(log, delimiter=';')

            for linha in reader:
                """
                Leitura dos componentes do .csv para atribuicao aos objetos
                """
                self.aluno = linha[2]
                TEMPO = linha[3]
                foco = linha[6]
                tmp = foco.split(':')
                QUESTAO = str(tmp[0] + tmp[1])
                DIFC = str(tmp[2])
                RESPOSTA = QUESTAO + ':' + str(tmp[4])
                tmp2 = tmp[3].split('-')
                DISCIPLINA = str(tmp2[0])
                TOPICO = str(tmp2[1])

                """
                criacao dos objetos de lugares
                
                faz uma verificacao se o lugar ja existe no map de lugares
                se existir ele incrementa o contador do lugar com +1
                senao, ele insere o lugar novo e inicia o contador com 1
                """

                placeQ = PNetPlace(QUESTAO, DISCIPLINA, TOPICO, DIFC, TEMPO)

                self.tupla1 = (QUESTAO, placeQ)
                self.tupla1[1].count += 1

                for item in self.net.listP:
                    if self.tupla1[0] == item[0]:
                        item[1].count += 1
                        self.tupla1 = item
                    else:
                        self.net.addPlace(self.tupla1)

                """if tupla1[0] in self.net.listP[range(0, len(self.net.listP))][0]:
                    index = self.net.listP[range(0, len(self.net.listP))][0].index(tupla1[0])
                    self.net.listP[index][1].count += 1
                    tupla1[1].count = self.net.listP[index][1].count
                else:
                    self.net.addPlace(tupla1)"""

                placeR = PNetPlace(RESPOSTA, None, None, None, TEMPO)

                self.tupla2 = (RESPOSTA, placeR)
                self.tupla2[1].count += 1

                for item in self.net.listP:
                    if self.tupla2[0] == item[0]:
                        item[1].count += 1
                        self.tupla2 = item
                    else:
                        self.net.addPlace(self.tupla2)

                """if tupla2 in self.net.listP:
                    index = self.net.listP.index(tupla2)
                    self.net.listP[index][1].count += 1
                    tupla2[1].count = self.net.listP[index][1].count
                else:
                    self.net.addPlace(tupla2)"""

                """
                Criacao dos objetos de Arcos.
                """

                arc1 = PNetArc(last, self.tupla1, self.tupla1[1].count, self.net)
                arc2 = PNetArc(self.tupla1, self.net.listT[last[0] + 1],
                               self.tupla1[1].count, self.net)
                arc3 = PNetArc(self.net.listT[last[0] + 1], self.tupla2,
                               self.tupla2[1].count, self.net)
                arc4 = PNetArc(self.tupla2, self.net.listT[last[0] + 2],
                               self.tupla2[1].count, self.net)

                self.net.addArc(arc1)
                self.net.addArc(arc2)
                self.net.addArc(arc3)
                self.net.addArc(arc4)

                last = self.net.listT[last[0] + 2]

            placeSS = PNetPlace('SS', None, None, None, None)
            placeSS.count += 1
            tuplaSS = ('SS', placeSS)
            self.net.addPlace(tuplaSS)

            arcSS = PNetArc(last, tuplaSS, tuplaSS[1].count,
                            self.net)
            self.net.addArc(arcSS)

            self.net.id = self.aluno

        log.close()

        #self.net.orderedMaps()

        return self.net
