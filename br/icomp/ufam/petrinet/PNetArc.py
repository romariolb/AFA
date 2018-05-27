import time  # timestamp for id generation
from random import randint  # random number for id generation

class PNetArc:

    def __init__(self, source, target,  inscription, net):
        self.id = (str(time.time())) + str(randint(0, 1000))
        self.source = source
        self.target = target
        self.inscription = inscription
        self.net = net

    def find_source(self):
        if self.source in self.net.listT:
            return self.net.listT[self.source]
        else:
            return self.net.listP[self.source]

    def find_target(self):
        if self.target in self.net.listT:
            return self.net.listT[self.target]
        else:
            return self.net.listP[self.target]

    def __str__(self):
        return str(self.id) + '| ' + str(self.find_source().node.name) + "-->" + str(self.find_target().node.name) + '| '\
               + str(self.inscription)
