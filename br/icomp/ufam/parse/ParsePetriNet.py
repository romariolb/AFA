import csv
from br.icomp.ufam.petrinet.PNet import PNet
from br.icomp.ufam.petrinet.PNetPlace import PNetPlace
from br.icomp.ufam.petrinet.PNetTransition import PNetTransition
from br.icomp.ufam.petrinet.PNetArc import PNetArc

def isInFOut(question, f_out):
    if f_out != []:
        for item in f_out:
            if question == item[0]:
                indice = f_out.index(item)
                return indice
            else:
                pass
    else:
        return False
    return False


def isCorrectCount(question, f_out):
    inFOut = isInFOut(question, f_out)
    if inFOut != False:
        f_out[inFOut][1] += 1
        return f_out
    else:
        f_out.append([str(question), 1])
        return f_out
    return f_out
    """if f_out != []:
        for item in f_out:
            if question == item[0]:
                indice = f_out.index(item)
                f_out[indice][1] += 1
            else:
                print('entrou no else')
                f_out.append([str(question), 1])
    else:
        f_out.append([str(question), 1])
    return f_out"""


def returnArc(source, target, net):
    """

    :param source: ["id", obj]
    :param target: ["id", obj]
    :param net: PNet
    :return: obj

    Com isso, voce consegue o obj individual de cada arco criado
    Assim, voce so precisa receber esse obj e pegar o atributo
    inscription. Ex: var = returnArc(pair_lugar, pair_transition, net)
    print(str(var.inscription))
    """
    for arc in net.listA:
        if source[0] == arc.source[0] and target[0] == arc.target[0]:
            return arc
        else:
            pass


def hasIn_listP(pair, net, dev):
    """
    Verifica se um lugar ja existe na lista de lugares

    :param dev: int
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
            net.listP[i][1].desvio = dev
            pair = item
            return pair
        else:
            pass
    return 0


def hasIn_gabList(pair, answers):
    """
    verifica se o lugar de resposta eh a desejada no gabarito.
    Cria retorna 1 se sim
    0 senao.

    :param pair: [questao, respostas]
    :param answers: questao, resposta
    :return: 1||0
    """
    for item in answers:
        if pair[0] == item[0]:
            # print('igual\n')
            return 1
    return 0


def return_index(strid, net):
    """
    retorna o indice de um lugar, se ele existir.
    :param strid: id
    :param net: PNet
    :return:
    """
    for item in net.listP:
        if strid == item[0]:
            indice = net.listP.index(item)
            return indice
    return 0


def verify_deviation(question, answer, str_file):
    """
    verifica o deviation da resposta
    :param question: str
    :param answer: str
    :param str_file: arg
    :return:
    """
    f_input = open(str_file, 'r')
    for line in f_input:
        q, ra, rb, rc, rd, re, d1, d2, d3, t = line.replace("\n", "").split(" ")
        if question == int(q):
            if answer == 'A':
                f_input.close()
                if ra != '0':
                    return int(ra)
                else:
                    return 0
                # return int(ra)
            elif answer == 'B':
                f_input.close()
                if rb != '0':
                    return int(rb)
                else:
                    return 0
                # return int(rb)
            elif answer == 'C':
                f_input.close()
                if rc != '0':
                    return int(rc)
                else:
                    return 0
                # return int(rc)
            elif answer == 'D':
                f_input.close()
                if rd != '0':
                    return int(rd)
                else:
                    return 0
                # return int(rd)
            elif answer == 'E':
                f_input.close()
                if re != '0':
                    return int(re)
                else:
                    return 0
                # return int(re)
            else:
                f_input.close()
                return 0


class ParsePetriNet:

    def __init__(self, f_input):
        self.student = None
        self.net = PNet()
        self.f_input = f_input
        
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

    @staticmethod
    def returnArc(source, target, net):
        """

        :param source: ["id", obj]
        :param target: ["id", obj]
        :param net: PNet
        :return: obj

        Com isso, voce consegue o obj individual de cada arco criado
        Assim, voce so precisa receber esse obj e pegar o atributo
        inscription. Ex: var = returnArc(pair_lugar, pair_transition, net)
        print(str(var.inscription))
        """
        for arc in net.listA:
            if source[0] == arc.source[0] and target[0] == arc.target[0]:
                return arc
            else:
                pass

    def parse_csv_file(self, file, answers_list):

        answers = answers_list

        # print('entrou no metodo parse_csv')

        # self.net = PNet()

        # print('instaciou obj NET')
        """
        cria os estados de verificacao, para que eles fiquem nas primeiras
        posicoes do vetor.
        """
        for item in answers:
            # indice = answers.index(item) + 1
            Nome = item[2] + 'V'
            # print(Nome)
            p = PNetPlace(Nome, None, None, None, None)
            t = [Nome, p]

            self.net.addPlace(t)
        """
        Cria o estado S, transicao 0 e primeiro arco, inicial.
        """
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

        """
        Cria as transicoes. 2 x MAX(linhas do arquivo).
        """
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
                self.student = linha[6]
                TEMPO = linha[7]
                foco = linha[10]
                tmp = foco.split(':')
                QUESTAO = str(tmp[0] + tmp[1])
                q_n = int(tmp[1])
                DIFC = str(tmp[2])
                RESPOSTA = QUESTAO + str(tmp[4])
                r_n = str(tmp[4])
                tmp2 = tmp[3].split('-')
                DISCIPLINA = str(tmp2[0])
                TOPICO = str(tmp2[1])

                """
                criacao dos objetos de lugares
                
                faz uma verificacao se o lugar ja existe no map de lugares
                se existir ele incrementa o contador do lugar com +1
                senao, ele insere o lugar novo e inicia o contador com 1
                """

                dev = verify_deviation(q_n, r_n, self.f_input)

                placeQ = PNetPlace(QUESTAO, DISCIPLINA, TOPICO, DIFC, TEMPO)

                pair1 = [QUESTAO, placeQ]
                pair1[1].count += 1

                verify = hasIn_listP(pair1, self.net, dev)

                """
                Verifica se o par (id_place, obj_place) Questao ja existe.
                Se existir ele eh retornado para variavel temporaria
                senao o par eh adicionado lista de Lugares.
                """
                if verify != 0:
                    pair1 = verify
                else:
                    # print(placeQ.id)
                    self.net.addPlace(pair1)

                placeR = PNetPlace(RESPOSTA, None, None, None, TEMPO)

                placeR.deviation = dev

                pair2 = [RESPOSTA, placeR]
                pair2[1].count += 1

                verifyR = hasIn_listP(pair2, self.net, dev)
                verifyG = hasIn_gabList(pair2, answers)

                """
                Verifica se o par (id_place, obj_place) resposta ja existe.
                Se existir ele eh retornado para variavel temporaria
                senao o par eh adicionado lista de Lugares.
                """
                if verifyR != 0:
                    pair2 = verifyR
                else:
                    self.net.addPlace(pair2)

                """
                Criacao dos objetos de Arcos.
                """

                i = return_index(QUESTAO + 'V', self.net)

                if verifyG == 1:

                    """
                    Entra aqui se a resposta for a desejada. Aqui e onde cria o arco para o lugar de verificacao.
                    posso contar quantas vezes o aluno passou pela correta aqui
                    """
                    # print(QUESTAO)
                    # print(self.net.getFOut())
                    self.net.f_out = isCorrectCount(QUESTAO, self.net.f_out)

                    if self.net.listP[i][1].last == 1:
                        arc0 = PNetArc(self.net.listP[i], last, self.net.listP[i][1].count, self.net)
                        self.net.listT[last[0]][1].preBinding.append(self.net.listP[i])
                        # add o lugar necessario para disparo de transicao
                        self.net.addArc(arc0)

                    self.net.listP[i][1].count += 1
                    self.net.listP[i][1].last = 1
                    self.net.listP[i][1].time = TEMPO

                    pair3 = self.net.listP[i]

                    arc1 = PNetArc(last, pair1, pair1[1].count, self.net)
                    arc2 = PNetArc(pair1, self.net.listT[last[0] + 1],
                                   pair1[1].count, self.net)
                    self.net.listT[last[0] + 1][1].preBinding.append(pair1)
                    arc3 = PNetArc(self.net.listT[last[0] + 1], pair2,
                                   pair2[1].count, self.net)
                    arc4 = PNetArc(self.net.listT[last[0] + 1], pair3,
                                   pair3[1].count, self.net)
                    arc5 = PNetArc(pair2, self.net.listT[last[0] + 2],
                                   pair2[1].count, self.net)
                    self.net.listT[last[0] + 2][1].preBinding.append(pair2)

                    self.net.addArc(arc1)
                    self.net.addArc(arc2)
                    self.net.addArc(arc3)
                    self.net.addArc(arc4)
                    self.net.addArc(arc5)

                    last = self.net.listT[last[0] + 2]


                else:

                    if self.net.listP[i][1].last == 1:
                        arc0 = PNetArc(self.net.listP[i], last, self.net.listP[i][1].count, self.net)
                        self.net.listT[last[0]][1].preBinding.append(self.net.listP[i])
                        self.net.addArc(arc0)
                        self.net.listP[i][1].last = 0

                    arc1 = PNetArc(last, pair1, pair1[1].count, self.net)
                    arc2 = PNetArc(pair1, self.net.listT[last[0] + 1],
                                   pair1[1].count, self.net)
                    self.net.listT[last[0] + 1][1].preBinding.append(pair1)
                    arc3 = PNetArc(self.net.listT[last[0] + 1], pair2,
                                   pair2[1].count, self.net)
                    arc4 = PNetArc(pair2, self.net.listT[last[0] + 2],
                                   pair2[1].count, self.net)
                    self.net.listT[last[0] + 2][1].preBinding.append(pair2)

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
