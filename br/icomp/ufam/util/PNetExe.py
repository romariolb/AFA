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


def sumMarking(marking, matrix, index):
    """

    :param index: int
    :param marking: List
    :param matrix: List
    :return: List
    """

    nextMark = []
    Input = []
    Output = []

    Input = matrix.matrizI[index]
    Output = matrix.matrizO[index]

    # print(str(marking) + '-\n' + str(Input) + '+\n' + str(Output) + '\n')

    for i in range(len(marking)):
        out = marking[i] - Input[i] + Output[i]
        nextMark.append(out)

    return nextMark


class PNetExe:

    def __init__(self, matrix, numQuestions, n_f):
        """

        :param matrix: Matrix
        """
        self.matrix = matrix
        self.numQuestions = numQuestions - n_f
        self.marking = []
        self.transitions = []
        self.index = 0

    def __str__(self):
        text = '---\n'

        # text += str(self.marking) + '\n'

        # text += str(self.transitions) + '\n'

        # text += str(self.calculation()) + '\n'

        return text

    def initMark(self):
        size = self.matrix.colunas
        print(str(size))
        for i in range(size):
            if i == self.numQuestions:
                self.marking.append(1)
            else:
                self.marking.append(0)

        for item in range(self.matrix.linhas):
            self.transitions.append(0)

    def enabledTransition(self):
        # matrixInput = self.matrix.matrizI

        for i in range(self.matrix.linhas):
            self.transitions[i] = 0

        """for mark in range(len(self.marking)):
            if self.marking[mark] != 0:
                # print('Mark = ' + str(mark))
                for t in range(self.matrix.linhas):
                    # print('  Buscando na linha ' + str(t) + ' na coluna ' + str(mark))
                    if self.matrix.matrizI[t][mark] == self.marking[mark]:  # <= NESSA LINHA
                        # print('   Encontrei!')
                        self.transitions[t] = self.matrix.matrizI[t][mark]
                    #              print(self.matrix.matrizI[t])
                    else:
                        # print('  n encontrei')
                        # print(str('   ' + str(self.matrix.matrizI[t][mark])))
                        pass
            else:
                pass"""

        for mark in range(len(self.marking)):
            if self.marking[mark] != 0:
                for t in range(self.matrix.linhas):
                    if self.matrix.matrizI[t][mark] == self.marking[mark]:
                        preBinding = self.matrix.net.listT[t][1].preBinding
                        length = len(preBinding)
                        count = 0
                        for binding in preBinding:
                            index = self.matrix.net.listP.index(binding)
                            weight = self.matrix.net.return_weigth(binding, self.matrix.net.listT[t])
                            if self.marking[index] == weight:
                                count += 1
                            else:
                                pass
                        if count == length:
                            self.transitions[t] = self.matrix.matrizI[t][mark]
                            self.index = t
                        else:
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
        # print('=> ' + str(self.transitions))
        # print('-> ' + str(self.marking))
        self.enabledTransition()

        if self.haveTransitions() != 0:
            # matrixR = prodMatrix(self.matrix.matrixD, self.transitions).tolist()
            # noinspection PyTypeChecker
            nextMark = sumMarking(self.marking, self.matrix, self.index)
            self.marking = nextMark

            self.calculation()

        else:
            print('!!!!!!!!\n ' + str(self.marking))
