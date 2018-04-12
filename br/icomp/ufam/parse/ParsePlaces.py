import time  # timestamp for id generation
from random import randint  # random number for id generation


class Place:
    """ This class represents a labelled Place of a Petri net.

    A place represents a resource.

    place.id: Unique ID of this place.
    place.label: Label of this place.
    place.marking: Current marking of this place.
      Usually a marking is the count of tokens contained into this place.

    Layout information:
      place.position: Position to display the place in graphical representations.
        Usually a place is drawn as a circle. The position is the center of this circel.
      place.offset: Offest of the place label.
        Usually the label of a place is printed centered below the circle which
        represents the place in graphical representations. This offset represents
        a vector which defines a translation of the label inscription from its
        usual position.
    """

    def __init__(self):
        self.label = "Place"  # default label of event
        # generate a unique id
        self.id = ("Place" + str(time.time())) + str(randint(0, 1000))
        self.type = ''
        self.marking = ''

    def __str__(self):
        return str(self.id) + '| ' + self.label + '| ' + str(self.marking) \
               + '| ' + self.type
