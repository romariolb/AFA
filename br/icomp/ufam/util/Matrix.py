class Matrix:

    def __init__(self, pnet):
        """

        :type pnet: PNet
        """
        self.pnet = pnet
        self.arcs = self.pnet.listA
        self.linhas = len(pnet.listP)
        self.colunas = len(pnet.listT)
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
        Verifica relação de Input

        Verifica se existe uma ligação de incidência de um lugar
        para uma transição.

        :param i: key
        :param j: key
        :return: true, false
        """
        place = self.pnet.listP.get(i)
        transition = self.pnet.listT.get(j)
        for arc in self.arcs:
            if place.node.id in arc.source and transition.node.id in arc.target:
                return True
        return False

    def hasArcO(self, i, j):
        """
        Verifica relação de Output

        Verifica se existe uma ligação de incidência de uma transição
        para um lugar.

        :param i: int
        :param j: int
        :return: true, false
        """

        place = self.pnet.listP.get(i)
        transition = self.pnet.listT.get(j)
        for arc in self.arcs:
            if transition.node.id in arc.source and place.node.id in arc.target:
                return True
        return False

    def setMatrixI(self):
        """
        Gera a matriz de input da rede.

        :return:
        """
        for place in self.pnet.listP:
            linha = []
            for transition in self.pnet.listT:
                if self.hasArcI(place, transition) is True:
                    linha.append(1)
                else:
                    linha.append(0)
            self.matrizI.append(linha)

    def setMatrixO(self):
        """
        Gera a matriz de output da rede.

        :return:
        """
        for place in self.pnet.listP:
            linha = []
            for transition in self.pnet.listT:
                if self.hasArcO(place, transition) is True:
                    linha.append(1)
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
