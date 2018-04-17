class Matrix:

    def __init__(self, PNet):
        self.PNet = PNet
        self.arcs = PNet.listA
        self.linhas = len(PNet.listP)
        self.colunas = len(PNet.listT)
        self.matriz = []

    """def setMatrix(self):
        for i in range(1, self.linhas+1):
            tmp = []
            for j in range(1, self.colunas+1):
                if"""