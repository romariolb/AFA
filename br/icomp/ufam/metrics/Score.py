def findPlace(index, net):
    for item in net.listP:
        if item[0] == 'Q' + str(index + 1):
            return item
        else:
            pass


class Score:
    def __init__(self, marking, numQuestions, net):
        """

        :type net: PNet
        :param marking: list
        :param numQuestions: int
        """
        self.finalMark = marking
        self.numQuestions = numQuestions
        self.net = net
        self.numCorrects = 0
        self.corrects = []
        self.incorrect = []
        self.score = 0

    def __str__(self):
        text = 'Voce conseguiu acertar {} de {} questoes e sua pontuacao foi de {} pontos\n'.format(self.numCorrects,
                                                                                                    self.numQuestions,
                                                                                                    self.score)
        text += 'ACERTADAS: \n'
        for i in self.corrects:
            text += str(i) + '\n'
        return text

    def calculus(self):
        for i in range(self.numQuestions):
            if self.finalMark[i] != 0:
                self.numCorrects += 1
                self.corrects.append(findPlace(i, self.net))
            else:
                self.incorrect.append(findPlace(i, self.net))
        self.score = float((10.0 / self.numQuestions) * self.numCorrects)
