import time  # timestamp for id generation
from random import randint  # random number for id generation


class PNetArc:

    def __init__(self, source, target, inscription, net):
        """
        :param source: tuple
        :param target: tuple
        :param inscription: int
        :param net: object
        """
        self.id = (str(time.time())) + str(randint(0, 1000))
        self.source = source
        self.target = target
        self.inscription = inscription
        self.net = net

    def find_source(self):
        if self.source in self.net.listT:
            index = self.net.listT.index(self.source)
            return self.net.listT[index][1]
        else:
            index = self.net.listP.index(self.source)
            return self.net.listP[index][1]

    def find_target(self):
        if self.target in self.net.listT:
            index = self.net.listT.index(self.target)
            return self.net.listT[index][1]
        else:
            index = self.net.listP.index(self.target)
            return self.net.listP[index][1]

    def __str__(self):
        return str(self.find_source().name) + "-->" + str(self.find_target().name) + \
               '| ' + str(self.inscription)
