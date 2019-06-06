from br.icomp.ufam.petrinet.PNetPlace import PNetPlace


def findPlace(index, answers_list, net):
    tmp = answers_list[index]
    # print(tmp)
    tmp2 = tmp[2]
    # tmp = tmp2[0]

    for item in net.listP:
        # print('{} {}'.format(item[0], tmp2))
        if item[0] == tmp2:
            return item
        else:
            pass
    return 0


class Score:
    def __init__(self, marking, numQuestions, net, n_f, answers_list):
        """

        :type net: PNet
        :param marking: list
        :param numQuestions: int
        """
        self.finalMark = marking
        self.numQuestions = numQuestions - n_f
        self.net = net
        self.answers_list = answers_list
        self.numCorrects = 0
        self.corrects = []
        self.incorrect = []
        self.score = 0

    def __str__(self):
        text = 'Voce conseguiu acertar {} de {} questoes e sua PONTUACAO foi de {} pontos\n'.format(self.numCorrects,
                                                                                                    self.numQuestions,
                                                                                                    round(self.score, 2))
        text += 'ACERTADAS: \n'
        for i in self.corrects:
            text += str(i[0]) + '\t'

        """text += 'ERRADAS: \n'
        for i in self.incorrect:
            text += str(i[0]) + '\n'"""
        return text

    def calculus(self):
        # print(self.answers_list)
        for i in range(0, self.numQuestions):
            if self.finalMark[i] > 0 and i != self.finalMark.index(self.finalMark[-1]): # exclui o SS
                self.numCorrects += 1
                tmp = findPlace(i, self.answers_list, self.net)
                # print(findPlace(i, self.net))
                if tmp != 0:
                    # print('tmp != 0')
                    self.corrects.append(tmp)
                else:
                    # print('tmp == 0')
                    pass
            elif self.finalMark[i] == 0 and i != self.finalMark.index(self.finalMark[self.numQuestions + 1]): # exclui o S
                tmp = findPlace(i, self.answers_list, self.net)
                if tmp != 0:
                    self.incorrect.append(tmp)
                else:
                    pass
            else:
                pass
        self.score = float((10.0 / self.numQuestions) * self.numCorrects)

    def getCorrects(self):
        return self.corrects
    def getIncorrect(self):
        return self.incorrect
