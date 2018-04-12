import time  # timestamp for id generation
from random import randint  # random number for id generation


class Edge:
    """ This class represents an arc of a Petri net.

    An edge represents an relation between a place and a transition or a transition
    and a place.

    edge.id: Unique ID of this edge.
    edge.source: ID of the source (start) node of this edge.
    edge.target: ID of the target (end) node of this edge.
    edge.inscription: Inscription of this edge.
      The inscription is usually an integer which is interpreted as weight of this edge.
    edge.net: The Petri net which contains this edge.
      This reference is used for the label resolution of the source and target events.
      See __str__ method.
    """

    def __init__(self):
        # generate a unique id
        self.id = ("Arc" + str(time.time())) + str(randint(0, 1000))
        self.source = None  # id of the source event of this arc
        self.target = None  # id of the target event of this arc
        self.inscription = ''  # inscription of this arc
        self.net = None  # Reference to net object for label resolution of source an target

    def find_source(self):
        if self.source in self.net.transitions:
            return self.net.transitions[self.source]
        else:
            return self.net.places[self.source]

    def find_target(self):
        if self.target in self.net.transitions:
            return self.net.transitions[self.target]
        else:
            return self.net.places[self.target]

    def __str__(self):
        return str(self.id) + '| ' + str(self.find_source().label) + "-->" + str(self.find_target().label) + '| '\
               + str(self.inscription)
