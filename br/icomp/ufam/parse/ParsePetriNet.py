import csv
from br.icomp.ufam.petrinet.PNet import PNet
from br.icomp.ufam.petrinet.PNetPlace import PNetPlace
from br.icomp.ufam.petrinet.PNetTransition import PNetTransition
from br.icomp.ufam.petrinet.PNetArc import PNetArc


def hasIn_listP(pair, net):
    """

    :param net: PNet
    :param pair: list
    :return: tupla: list || 0
    """
    for item in net.listP:
        # print(pair[0] + ' ' + item[0])
        if pair[0] == item[0]:
            # print('igual')
            i = net.listP.index(item)
            net.listP[i][1].count += 1
            pair = item
            return pair
        else:
            pass
    return 0


def hasIn_gabList(pair, answers):
    for item in answers:
        if pair[0] == item[0]:
            return 1
    return 0


def return_index(strid, net):
    for item in net.listP:
        if strid == item[0]:
            indice = net.listP.index(item)
            return indice
    return 0


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
        self.student = None
        self.net = PNet()
        # print('criou obj NET {}'.format(self.net))

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

    def parse_csv_file(self, file, answers_list):

        answers = answers_list

        # print('entrou no metodo parse_csv')

        # self.net = PNet()

        # print('instaciou obj NET')

        for item in answers:
            indice = answers.index(item) + 1
            Nome = 'Q' + str(indice) + 'V'
            p = PNetPlace(Nome, None, None, None, None)
            t = [Nome, p]

            self.net.addPlace(t)

        placeS = PNetPlace('S', None, None, None, None)
        placeS.count += 1
        pairS = ['S', placeS]
        self.net.addPlace(pairS)

        # print('criou o 1 lugar S')

        transition0 = PNetTransition(0)
        pair0 = [0, transition0]
        self.net.addTransition(pair0)

        # print('criou a primeira transicao')

        arcS = PNetArc(pairS, pair0,
                       pairS[1].count, self.net)
        self.net.addArc(arcS)

        # print('criou o 1 arco')

        with open(file, 'r') as log:
            t_max = sum(1 for row in log)
            t_max = t_max * 2

            """
            Criacao dos objetos de transicao.
            O numero total de transicoes eh o dobro de linhas do arquivo
            """
            for t in range(1, t_max + 1):
                transition1 = [t, PNetTransition(t)]
                self.net.addTransition(transition1)
            # print('criou as transicoes')

        log.close()

        with open(file, 'r') as log:

            last = self.net.listT[0]

            reader = csv.reader(log, delimiter=';')

            for linha in reader:
                """
                Leitura dos componentes do .csv para atribuicao aos objetos
                """
                self.student = linha[2]
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
                criacao dos objetos de lugares
                
                faz uma verificacao se o lugar ja existe no map de lugares
                se existir ele incrementa o contador do lugar com +1
                senao, ele insere o lugar novo e inicia o contador com 1
                """

                placeQ = PNetPlace(QUESTAO, DISCIPLINA, TOPICO, DIFC, TEMPO)

                pair1 = [QUESTAO, placeQ]
                pair1[1].count += 1

                verify = hasIn_listP(pair1, self.net)

                if verify != 0:
                    pair1 = verify
                else:
                    self.net.addPlace(pair1)

                placeR = PNetPlace(RESPOSTA, None, None, None, TEMPO)

                pair2 = [RESPOSTA, placeR]
                pair2[1].count += 1

                verifyR = hasIn_listP(pair2, self.net)
                verifyG = hasIn_gabList(pair2, answers)

                if verifyR != 0:
                    pair2 = verifyR
                else:
                    self.net.addPlace(pair2)

                """
                Criacao dos objetos de Arcos.
                """

                i = return_index(QUESTAO + 'V', self.net)

                if verifyG == 1:
                    self.net.listP[i][1].count += 1
                    self.net.listP[i][1].last = 1
                    self.net.listP[i][1].time = TEMPO

                    pair3 = self.net.listP[i]

                    arc1 = PNetArc(last, pair1, pair1[1].count, self.net)
                    arc2 = PNetArc(pair1, self.net.listT[last[0] + 1],
                                   pair1[1].count, self.net)
                    arc3 = PNetArc(self.net.listT[last[0] + 1], pair2,
                                   pair2[1].count, self.net)
                    arc4 = PNetArc(self.net.listT[last[0] + 1], pair3,
                                   pair3[1].count, self.net)
                    arc5 = PNetArc(pair2, self.net.listT[last[0] + 2],
                                   pair2[1].count, self.net)

                    self.net.addArc(arc1)
                    self.net.addArc(arc2)
                    self.net.addArc(arc3)
                    self.net.addArc(arc4)
                    self.net.addArc(arc5)

                    last = self.net.listT[last[0] + 2]

                else:

                    if self.net.listP[i][1].last == 1:
                        arc0 = PNetArc(self.net.listP[i], last, self.net.listP[i][1].count, self.net)
                        self.net.addArc(arc0)
                        self.net.listP[i][1].last = 0

                    arc1 = PNetArc(last, pair1, pair1[1].count, self.net)
                    arc2 = PNetArc(pair1, self.net.listT[last[0] + 1],
                                   pair1[1].count, self.net)
                    arc3 = PNetArc(self.net.listT[last[0] + 1], pair2,
                                   pair2[1].count, self.net)
                    arc4 = PNetArc(pair2, self.net.listT[last[0] + 2],
                                   pair2[1].count, self.net)

                    self.net.addArc(arc1)
                    self.net.addArc(arc2)
                    self.net.addArc(arc3)
                    self.net.addArc(arc4)

                    last = self.net.listT[last[0] + 2]

            placeSS = PNetPlace('SS', None, None, None, None)
            placeSS.count += 1
            tuplaSS = ['SS', placeSS]
            self.net.addPlace(tuplaSS)

            arcSS = PNetArc(last, tuplaSS, tuplaSS[1].count,
                            self.net)
            self.net.addArc(arcSS)

            self.net.id = self.student

        log.close()

        # self.net.orderedMaps()

        return self.net
