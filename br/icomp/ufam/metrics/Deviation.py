
"""
10/numQuestoes = X | X = 60
desvio 0 -> 0%
desvio 2 -> %X |30%
desvio 3 -> %X |60%
desvio 4 -> %X |90%

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
                    if a2.target[1].desvio != d:
                        d = a2.target[1].desvio #o desvio vai de 0 a 4, soma os valores de desvio dividido pelo desvio maximo (qntd de questoes).
                    else:
                        pass
                else:
                    pass
        else:
            pass
    return d


class Deviation:
    def __init__(self, marking, numQuestions, net, score):
        """

        :type score: Score
        :type net: PNet
        :param marking: list
        :param numQuestions: int
        """
        self.finalMark = marking
        self.numQuestions = numQuestions - 5
        self.net = net
        self.numIncorrects = 0
        self.incorrect_dev = []
        self.incorrect = []
        self.scoreP = score
        self.score = float

    def __str__(self):
        text = 'Voce errou {} de {} questoes \n'.format(self.numIncorrects - 5,
                                                        self.numQuestions)
        text += 'ERRADAS: \n'
        for i in self.incorrect:
            text += str(i) + '\n'

        text += '\nDesvios:\n'
        for j in self.incorrect_dev:
            text += str(j) + '\n'

        text += '\nA nota dos seus desvios foi de: {}\n'.format(self.score)
        return text

    def listIncorrects(self):
        for i in range(1, self.numQuestions):
            if self.finalMark[i] == 0:
                self.numIncorrects += 1
                self.incorrect.append(findPlace(i, self.net))
            else:
                pass
        # self.score = float((10.0 / self.numQuestions) * self.numCorrects)

    def mapQuest(self):
        for q in self.incorrect:
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
        print('soma ', soma)

        temp = 4 * self.numQuestions
        print('temp ', temp)

        self.score = float(float(soma) / float(temp))
