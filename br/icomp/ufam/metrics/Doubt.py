from operator import itemgetter


def orderedList(uList):
    """

    :param uList: List
    :return:
    """
    oList = sorted(uList, key=itemgetter(2), reverse=True)
    return oList


class Doubt:
    def __init__(self, corrects, incorrect, qtd):
        """

        :param corrects: List
        :param incorrect: List
        """
        self.corrects = corrects
        self.incorrect = incorrect
        self.orderedCorrect = []
        self.orderedIncorrect = []
        self.qtd = qtd

    def __str__(self):
        text = 'Nivel de duvida:\nCorretas:\n'

        for item in self.orderedCorrect:
            text += str(item[0]) + ' | Retornos: ' + \
                    str(item[2]) + '\n'

        text += 'Incorretas:\n'

        for item in self.orderedIncorrect:
            text += str(item[0]) + ' | Retornos: ' + \
                    str(item[2]) + '\n'

        return text

    def doubtLevel(self):
        for i in range(len(self.corrects)):
            self.corrects[i].append(self.corrects[i][1].count)
        for i in range(len(self.incorrect)):
            self.incorrect[i].append(self.incorrect[i][1].count)

        x = orderedList(self.corrects)
        y = orderedList(self.incorrect)

        self.orderedCorrect = x[:self.qtd]
        self.orderedIncorrect = y[:self.qtd]
