class PNetPlace:

    def __init__(self, name, disciplina, topico, dificuldade, tempo):
        # self.node = PNetNode(id, name)
        self.id = name
        self.name = name
        self.discipline = disciplina
        self.topic = topico
        self.difficulty = dificuldade
        self.deviation = 0
        self.time = tempo
        self.count = 0
        self.last = 0

    def __str__(self):
        return str(self.id) + '| ' + self.name + '| ' + str(self.time)
