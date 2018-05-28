import time  # timestamp for id generation
from random import randint  # random number for id generation


class PNetArc:

    def __init__(self, source, target, inscription, net):
        self.id = (str(time.time())) + str(randint(0, 1000))
        self.source = source
        self.target = target
        self.inscription = inscription
        self.net = net

    def find_source(self):
        if self.source.node.id in self.net.listT:
            return self.net.listT[self.source.node.id]
        else:
            return self.net.listP[self.source.node.id]

    def find_target(self):
        if self.target.node.id in self.net.listT:
            return self.net.listT[self.target.node.id]
        else:
            return self.net.listP[self.target.node.id]

    def __str__(self):
        return str(self.id) + '| ' + str(self.find_source().node.name) + "-->" + str(self.find_target().node.name) + \
               '| ' + str(self.inscription)
