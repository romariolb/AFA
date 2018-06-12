class PNetExe:

    def __init__(self, matrix, numQuestions):
        """

        :param matrix: Matrix
        """
        self.matrix = matrix
        self.numQuestions = numQuestions
        self.marking = []
        self.transitions = []
        self.matrixSub = []

    def __str__(self):
        text = '---\n'

        text += str(self.marking) + '\n'

        text += str(self.transitions) + '\n'

        return text

    def initMark(self):
        size = self.matrix.colunas
        for i in range(0, size):
            if i == self.numQuestions:
                self.marking.append(1)
            else:
                self.marking.append(0)

    def enabledTransition(self):
        # matrixInput = self.matrix.matrizI

        for item in range(0, self.matrix.linhas):
            self.transitions.append(0)

        for mark in self.marking:
            if mark != 0:
                i = self.marking.index(mark)
                for t in range(0, self.matrix.linhas):
                    if self.matrix.matrizI[t][i] == mark:
                        self.transitions[t] = self.matrix.matrizI[t][i]
                    else:
                        pass
            else:
                pass
