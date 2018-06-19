import time  # timestamp for id generation
from random import randint  # random number for id generation
from br.icomp.ufam.petrinet.PNetNode import PNetNode


class PNetTransition:

    def __init__(self, ID):
        # self.node = PNetNode(ID, 'T' + str(ID))
        self.id = ID
        self.name = 'T' + str(ID)
        self.preBinding = []

    def __str__(self):
        return str(self.name)

