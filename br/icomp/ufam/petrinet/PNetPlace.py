from br.icomp.ufam.petrinet.PNetNode import PNetNode


class PNetPlace:

    def __init__(self, id, name, type, initMarking):
        self.node = PNetNode(id, name)
        self.type = type
        self.initMarking = initMarking

    def __str__(self):
        return str(self.node.id) + '| ' + self.node.name + '| ' + str(self.initMarking) \
               + '| ' + self.type
