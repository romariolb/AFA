from br.icomp.ufam.petrinet.PNetNode import PNetNode


class PNetTransition:

    def __init__(self, id, name, expGuard, code):
        self.node = PNetNode(id, name)
        self.expGuard = expGuard
        #self.preBinding = preBinding
        #self.var = var
        self.code = code

    def __str__(self):
        return str(self.node.id) + '| ' + self.node.name + '| ' + str(self.expGuard) + '| ' + str(self.code)

