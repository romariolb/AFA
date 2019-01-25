
"""
10/numQuestoes = X | X = 60
deviation 0 -> 0%
deviation 1 -> %X |30%
deviation 2 -> %X |60%
deviation 3 -> %X |90%
deviation 4 -> %x |100%

"""


def findPlace(index, net):
    for item in net.listP:
        if item[0] == 'Q' + str(index + 1):
            return item
        else:
            pass


def findArcSource(question, net):
    d = 0
    for a1 in net.listA:
        if question[0] == a1.source[0]:  # questao
            for a2 in net.listA:
                if a1.target[0] == a2.source[0]:  # transicao
                    if a2.target[1].deviation != d:
                        d = a2.target[1].deviation #o deviation vai de 0 a 4, soma os valores de deviation dividido pelo deviation maximo (qntd de questoes).
                    else:
                        pass
                else:
                    pass
        else:
            pass
    return d


class Deviation:
    def __init__(self, marking, numQuestions, net, score, n_f, w_s, incorrect):
        """

        :type score: Score
        :type net: PNet
        :param marking: list
        :param numQuestions: int
        """
        self.finalMark = marking
        self.numQuestions = numQuestions - n_f
        self.net = net
        self.numIncorrects = 0
        self.incorrect_dev = []
        self.incorrect = incorrect
        self.scoreP = score
        self.scoreWS = w_s
        self.scoreD = float

    def __str__(self):
        text = 'Voce errou {} de {} questoes \n'.format(self.numIncorrects,
                                                        self.numQuestions)
        """text += 'ERRADAS: \n'
        for i in self.incorrect:
            text += str(i) + '\n'"""

        text += '\nDesvios [Questao, Desvio]:\n'
        for j in self.incorrect_dev:
            text += str(j) + '\n'

        text += '\nConforme sua NOTA PONDERADA ({})'.format(round(self.scoreWS, 2)) + \
                ' o percentual dos seus DESVIOS e de: {}%\n'.format(round(self.scoreD, 2))
        return text

    def listIncorrects(self):
        self.numIncorrects = len(self.incorrect)
        """for i in range(1, self.numQuestions):
            if self.finalMark[i] == 0:
                self.numIncorrects += 1
                self.incorrect.append(findPlace(i, self.net))
            else:
                pass"""
        # self.score = float((10.0 / self.numQuestions) * self.numCorrects)

    def mapQuest(self):
        for q in self.incorrect:
            print(str(q))
            if q is not None:
                d = findArcSource(q, self.net)
                self.incorrect_dev.append([q[0], d])
            else:
                pass

    def calculus(self):
        soma = 0
        # val_q = float(10.0 / self.numQuestions)
        # print('Cada questao vale: ' + str(val_q))
        for d in self.incorrect_dev:
            if d[1] == 3:
                soma += 3
            elif d[1] == 2:
                soma += 2
            elif d[1] == 1:
                soma += 1
            else:
                soma += 0

        tam = len(self.scoreP.corrects)

        soma += (4 * tam)
        # print('soma ', soma)

        # temp = 4 * self.numQuestions
        # print('temp ', temp)

        # self.scoreWS = float(float(soma) / float(temp)) * 10.0
        self.scoreD = float(10.0 - float(self.scoreWS)) * 10.0
