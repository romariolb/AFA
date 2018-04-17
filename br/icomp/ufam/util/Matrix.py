class Matrix:

    def __init__(self, pnet):
        """

        :type pnet: PNet
        """
        self.pnet = pnet
        self.arcs = pnet.listA
        self.linhas = len(pnet.listP)
        self.colunas = len(pnet.listT)
        self.matrizI = []
        self.matrizO = []

    def hasArcI(self, i, j):
        """
        Verifica relação de Input

        Verifica se existe uma ligação de incidência de um lugar
        para uma transição.

        :param i: int
        :param j: int
        :return: true, false
        """
        place = self.pnet.listP[i]
        transition = self.pnet.listT[j]
        for arc in self.arcs:
            if place.node.id in arc.source.node.id and transition.node.id \
                    in arc.target.node.id:
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

        place = self.pnet.listP[i]
        transition = self.pnet.listT[j]
        for arc in self.arcs:
            if transition.node.id in arc.source.node.id and place.node.id \
                    in arc.target.node.id:
                return True
        return False

    def setMatrixI(self):
        """
        Matriz de Input

        Cria a matriz de incidência, verifica se um lugar
        tem relação com uma trasição.
        :return: None
        """
        for i in range(0, self.linhas):
            linha = []
            for j in range(0, self.colunas):
                if self.hasArcI(i, j) is True:
                    linha.append(1)
                else:
                    linha.append(0)
        self.matrizI.append(linha)

    def setMatrixO(self):
        """
        Matriz de Output

        Cria a matriz de saída, verifica se uma transição
        tem relação com um lugar.
        :return: None
        """
        for i in range(0, self.linhas):
            linha = []
            for j in range(0, self.colunas):
                if self.hasArcO(i, j) is True:
                    linha.append(1)
                else:
                    linha.append(0)
        self.matrizI.append(linha)
