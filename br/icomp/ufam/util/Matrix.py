class Matrix:

    def __init__(self, net):
        """

        :type pnet: PNet
        """
        self.net = net
        self.arcs = self.net.listA
        self.linhas = len(self.net.listT)
        self.colunas = len(self.net.listP)
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

        for linha in self.matrixD:
            text += str(linha) + '\n'

        return text

    def hasArcI(self, i, j):
        """
        Verifica relacao de Input

        Verifica se existe uma ligacao de incidencia de um lugar
        para uma transicao.

        :param i: key
        :param j: key
        :return: true, false
        """
        transition = i.node.id
        place = j.node.id
        for arc in self.arcs:
            if place == arc.source.node.id and transition == arc.target.node.id:
                return True
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

        transition = i.node.id
        place = j.node.id
        for arc in self.arcs:
            if transition == arc.source.node.id and place == arc.target.node.id:
                return True
        return False

    def setMatrixI(self):
        """
        Gera a matriz de input da rede.

        :return:
        """

        valuesP = self.net.listP.values()
        valuesT = self.net.listT.values()

        for transition in valuesT:
            linha = []
            for place in valuesP:
                if self.hasArcI(transition, place) is True:
                    linha.append(place.count)
                else:
                    linha.append(0)
            self.matrizI.append(linha)

    def setMatrixO(self):
        """
        Gera a matriz de output da rede.

        :return:
        """

        valuesP = self.net.listP.values()
        valuesT = self.net.listT.values()

        for transition in valuesT:
            linha = []
            for place in valuesP:
                if self.hasArcO(transition, place) is True:
                    linha.append(place.count)
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
