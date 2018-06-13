import numpy as np


def prodMatrix(matrix, transitions):
    """
    Multiplica duas matrizes.

    :param matrix: Matrix
    :param transitions: List
    :return: List
    """
    M1 = np.array(matrix)
    M2 = np.array(transitions)

    # matrixR = np.dot(M2, M1)

    return np.dot(M2, M1)


def sumMatrix(matrixR, marking):
    """

    :param matrixR: List
    :param marking: List
    :return: List
    """

    nextMark = []
    for i in range(len(marking)):
        nextMark.append(matrixR[i] + marking[i])

    return nextMark


class PNetExe:

    def __init__(self, matrix, numQuestions):
        """

        :param matrix: Matrix
        """
        self.matrix = matrix
        self.numQuestions = numQuestions
        self.marking = []
        self.transitions = []
        # self.matrixSub = []

    def __str__(self):
        text = '---\n'

        # text += str(self.marking) + '\n'

        # text += str(self.transitions) + '\n'

        # text += str(self.calculation()) + '\n'

        return text

    def initMark(self):
        size = self.matrix.colunas
        for i in range(size):
            if i == self.numQuestions:
                self.marking.append(1)
            else:
                self.marking.append(0)

        for item in range(self.matrix.linhas):
            self.transitions.append(0)

    def enabledTransition(self):
        # matrixInput = self.matrix.matrizI

        for item in range(self.matrix.linhas):
            self.transitions[item] = 0

        for mark in range(len(self.marking)):
            if self.marking[mark] != 0:
                # print('Mark = ' + str(mark))
                for t in range(self.matrix.linhas):
                    # print('  Buscando na linha ' + str(t) + ' na coluna ' + str(mark))
                    if self.matrix.matrizI[t][mark] == self.marking[mark]:
                        # print('   Encontrei!')
                        self.transitions[t] = self.matrix.matrizI[t][mark]
                    #              print(self.matrix.matrizI[t])
                    else:
                        # print('  n encontrei')
                        # print(str('   ' + str(self.matrix.matrizI[t][mark])))
                        pass
            else:
                pass

    def haveTransitions(self):
        check = 0
        for item in self.transitions:
            if item != 0:
                check = 1
                return check
            else:
                pass
        return check

    def calculation(self):
        print('=> ' + str(self.transitions))
        print('-> ' + str(self.marking))
        self.enabledTransition()

        if self.haveTransitions() != 0:
            matrixR = prodMatrix(self.matrix.matrixD, self.transitions).tolist()
            # noinspection PyTypeChecker
            nextMark = sumMatrix(matrixR, self.marking)
            self.marking = nextMark

            self.calculation()

        else:
            print('!!!!!!!!\n ' + str(self.marking))
