import time  # timestamp for id generation
from random import randint  # random number for id generation
from br.icomp.ufam.petrinet.PNetNode import PNetNode


class PNetPlace:

    def __init__(self, name, disciplina, topico, dificuldade, tempo):
        # self.node = PNetNode(id, name)
        self.id = name
        self.name = name
        self.disciplina = disciplina
        self.topico = topico
        self.dificuldade = dificuldade
        self.time = tempo
        self.count = 0

    def __str__(self):
        return str(self.id) + '| ' + self.name + '| ' + str(self.time)
