import time  # timestamp for id generation
from random import randint  # random number for id generation


class PNetTransition:

    def __init__(self):
        self.id = (str(time.time())) + str(randint(0, 1000))

    def __str__(self):
        return str(self.id)

