import time  # timestamp for id generation
from random import randint  # random number for id generation

class Type:

    def __init__(self):
        self.label = 'Type' # default label of event
        # generating a unique id
        self.id = ('Type' + str(time.time())) + str(randint(0, 1000))
        self.type = 'string' # default data type

    def __str__(self):
        return self.id + '| ' + self.label