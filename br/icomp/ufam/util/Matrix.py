

class Matrix:

    def __init__(self, net):
        """

        :type net: PNet
        """
        self.net = net
        # self.arcs = self.net.listA
        self.linhas = len(net.listT)
        self.colunas = len(net.listP)
        self.matrizI = []
        self.matrizO = []
        self.matrixD = []

    def __str__(self):
        text = '--- Matriz de input:\n'

        for linha in self.matrizI:
            text += str(linha) + '\n'

        text += '---Matriz de output:\n'

        for linha in self.matrizO:
            text += str(linha) + '\n'

        text += '---Matriz D:\n'

        # arr = np.array(self.matrixD)

        for linha in self.matrixD:
            text += str(linha) + '\n'

        return text

    def hasArcI(self, i, j):
        """
        Verifica relacao de Input

        Verifica se existe uma ligacao de incidencia de um lugar
        para uma transicao.

        :param i: list[key, obj]
        :param j: list[key, obj]
        :return: true, false
        """
        transition = i
        place = j
        for arc in self.net.listA:
            if place == arc.source and transition == arc.target:
                return arc.inscription
        return False

    def hasArcO(self, i, j):
        """
        Verifica relacao de Output

        Verifica se existe uma ligacao de incidencia de uma transicao
        para um lugar.

        :param i: int
        :param j: int
        :return: true, false
        """

        transition = i
        place = j
        for arc in self.net.listA:
            if transition == arc.source and place == arc.target:
                return arc.inscription
        return False

    def setMatrixI(self):
        """
        Gera a matriz de input da rede.

        :return:
        """

        valuesP = self.net.listP
        valuesT = self.net.listT

        for transition in valuesT:
            linha = []
            for place in valuesP:
                ins = self.hasArcI(transition, place)
                if ins is not False:
                    linha.append(ins)
                else:
                    linha.append(0)
            self.matrizI.append(linha)

    def setMatrixO(self):
        """
        Gera a matriz de output da rede.

        :return:
        """

        valuesP = self.net.listP
        valuesT = self.net.listT

        for transition in valuesT:
            linha = []
            for place in valuesP:
                ins = self.hasArcO(transition, place)
                if ins is not False:
                    linha.append(ins)
                else:
                    linha.append(0)
            self.matrizO.append(linha)

    def setMatrixD(self):
        """
        Gera a matriz D. Resultante de Output - Input

        :return:
        """
        for i in range(0, self.linhas):
            linha = []
            for j in range(0, self.colunas):
                sub = self.matrizO[i][j] - self.matrizI[i][j]
                linha.append(sub)
            self.matrixD.append(linha)
