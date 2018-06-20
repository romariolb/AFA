def orderedList(uList):
    """

    :param uList: List
    :return:
    """
    oList = sorted(uList, key=lambda x: 1)
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
                    str(item[1].count) + '\n'

        text += 'Incorretas:\n'

        for item in self.orderedIncorrect:
            text += str(item[0]) + ' | Retornos: ' + \
                    str(item[1].count) + '\n'

        return text

    def doubtLevel(self):
        x = orderedList(self.corrects)
        y = orderedList(self.incorrect)

        self.orderedCorrect = x[:self.qtd]
        self.orderedIncorrect = y[:self.qtd]
