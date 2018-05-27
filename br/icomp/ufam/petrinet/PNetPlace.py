from br.icomp.ufam.petrinet.PNetNode import PNetNode


class PNetPlace:

    def __init__(self, name, disciplina, topico, dificuldade, time):
        self.node = PNetNode(name)
        self.disciplina = disciplina
        self.topico = topico
        self.dificuldade = dificuldade
        self.time = time
        self.count = 0

    def __str__(self):
        return str(self.node.id) + '| ' + self.node.name + '| ' + str(self.time)
