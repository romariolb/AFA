import time  # timestamp for id generation
from random import randint  # random number for id generation


class PNet:

    def __init__(self):
        self.id = (str(time.time())) + str(randint(0, 1000))
        self.listP = []  # List of places. Tuple: place id, Value: place
        self.listT = []  # List of transitions. Tuple: transition id, Value: event
        self.listA = []  # List or arcs
        self.f_out = []  # Lista de quantas vezes o estudante passou por uma resposta correta
        # self.places = dict(ID='', name='', type='', initMarking='')
        # self.transitions = dict(ID='', name='', expGuard='', preBinding='', code='', var='')
        # self.arcs = dict(ID='', source='', target='', inscription='')

    def getFOut(self):
        return self.f_out
    
    def return_weigth(self, source, target):
        for arc in self.listA:
            if source == arc.source and target == arc.target:
                return arc.inscription
            else:
                pass

    '''
    Os lugares ficam salvos numa lista com varios dicionarios. Cada elemento da lista possui um dicionario
    com os mesmos cabecalhos, mas com valores diferentes. Futuramente, uma verificacao deve ser feita para
    evitar dados repetidos.
    '''

    def addPlace(self, place):
        """
        :type place: PNetPlace
        """
        # print('+p')
        self.listP.append(place)

    '''
    As transicoes ficam salvas numa lista com varios dicionarios. Cada elemento da lista possui um dicionario
    com os mesmos cabecalhos, mas com valores diferentes. Futuramente, uma verificacao deve ser feita para
    evitar dados repetidos.
    '''

    def addTransition(self, transition):
        """
        :type transition: PNetTransition
        """
        # print('+t')
        self.listT.append(transition)

    '''
    Os arcos ficam salvos numa lista com varios dicionarios. Cada elemento da lista possui um dicionario
    com os mesmos cabecalhos, mas com valores diferentes. Futuramente, uma verificacao deve ser feita para
    evitar dados repetidos.
    '''

    def addArc(self, arc):
        """
        :type arc: PNetArc
        """
        # print('+a')
        self.listA.append(arc)

    """def orderedMaps(self):
        self.listP = OrderedDict(sorted(self.listP.items(), key=lambda t: re.findall(r'\d+', t[0])))
        self.listT = OrderedDict(sorted(self.listT.items(), key=lambda t: t[0]))
    """

    def __str__(self):
        text = '\n--- Net:'
        text += str(self.id) + '\n'
        """text += '\nTransitions:\n'
        for transition in self.listT:
            text += str(transition[1].name) + ' | ' + str(transition[1].preBinding) + '\n'
        text += '\nPlaces:\n'
        for place in self.listP:
            text += str(place[0]) + ' ' + str(place[1].count) + '\n'
        text += '\nArcos:\n'
        for edge in self.listA:
            text += str(edge) + '\n'"""
        text += '---'

        return text
