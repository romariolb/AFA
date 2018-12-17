from br.icomp.ufam.petrinet.PNetPlace import PNetPlace


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
                        d = a2.target[1].deviation # o deviation vai de 0 a 4, soma os valores de deviation dividido pelo deviation maximo (qntd de questoes).
                    else:
                        pass
                else:
                    pass
        else:
            pass
    return d

class WeightedScore:
    def __init__(self, marking, numQuestions, net):
        """

        :type net: PNet
        :param marking: list
        :param numQuestions: int
        """
        self.finalMark = marking
        self.numQuestions = numQuestions - 5
        self.net = net
        self.numCorrects = 0
        self.numIncorrects = 0
        self.corrects = []
        self.incorrect = []
        self.incorrect_dev = []
        self.mp = self.numQuestions * 4
        self.count = 0
        self.score = 0

    def __str__(self):
        text = 'Voce conseguiu acertar {} de {} questoes e sua NOTA PONDERADA foi de {} pontos\n'.format(self.numCorrects,
                                                                                                    self.numQuestions,
                                                                                                    round(self.score, 2))
        """text += 'ACERTADAS: \n'
        for i in self.corrects:
            text += str(i) + '\n'"""

        text += 'mp = {} dev = {}\n'.format(self.mp, self.count)
        return text

    def listIncorrects(self):
        for i in range(1, self.numQuestions):
            if self.finalMark[i] == 0:
                self.numIncorrects += 1
                self.incorrect.append(findPlace(i, self.net))
            else:
                pass

    def mapQuest(self):
        for q in self.incorrect:
            if q is not None:
                d = findArcSource(q, self.net)
                self.incorrect_dev.append([q[0], d])
            else:
                pass

    def calculus(self):
        for i in range(self.numQuestions):
            if self.finalMark[i] != 0:
                self.numCorrects += 1
                self.corrects.append(findPlace(i, self.net))
                self.count += 4 # findPlace(i, self.net)[1].deviation
            else:
                self.incorrect.append(findPlace(i, self.net))
        for d in self.incorrect_dev:
            self.count += d[1]

        self.score = float(10.0 * (float(self.count) / float(self.mp)))

