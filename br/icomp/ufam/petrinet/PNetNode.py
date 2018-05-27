import time  # timestamp for id generation
from random import randint  # random number for id generation

class PNetNode:

    def __init__(self, name):
        self.id = (str(time.time())) + str(randint(0, 1000))
        self.name = name
