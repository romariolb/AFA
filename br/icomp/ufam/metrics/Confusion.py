class Confusion:
    def __init__(self, corrects, incorrect):
        """

        :param corrects: List
        :param incorrect: List
        """
        self.corrects = corrects
        self.incorrect = incorrect
        # self.orderedCorrect = []
        # self.orderedIncorrect = []
        #self.qtd = qtd
        self.sum = 0
        self.score = 0

    def __str__(self):
        text = 'Seu NIVEL DE CONFUSAO e de {}, com base na quantidade de marcacoes' \
               ' e questoes corretas da sua avaliacao.\n'.format(round(self.score, 2))

        return text

    def confusionLevel(self):
        # print(str(self.incorrect))
        for i in range(len(self.corrects)):
            self.corrects[i].append(self.corrects[i][1].count)
        for j in range(len(self.incorrect)):
            if self.incorrect[j] is not None:
                self.incorrect[j].append(self.incorrect[j][1].count)
            else:
                self.incorrect[j] = [0, 0, 0]
        for item in self.corrects:
            self.sum += item[2]
        for item in self.incorrect:
            self.sum += item[2]

    def calculus(self):
        self.score = float(1.0 - (float(len(self.corrects)) / float(self.sum)))