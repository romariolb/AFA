class PNet:

    def __init__(self, id):
        self.id = id
        self.listP = {}
        self.listT = {}
        self.listA = []
        self.listTy = []
        # self.places = dict(ID='', name='', type='', initMarking='')
        # self.transitions = dict(ID='', name='', expGuard='', preBinding='', code='', var='')
        # self.arcs = dict(ID='', source='', target='', inscription='')

    '''
    Os lugares ficam salvos numa lista com varios dicionários. Cada elemento da lista possui um dicionário
    com os mesmos cabeçalhos, mas com valores diferentes. Futuramente, uma verificação deve ser feita para
    evitar dados repetidos.
    '''

    def addPlace(self, place):
        """
        :type place: PNetPlace
        """

        self.listP[place.node.id] = place

    '''
    As transições ficam salvas numa lista com varios dicionários. Cada elemento da lista possui um dicionário
    com os mesmos cabeçalhos, mas com valores diferentes. Futuramente, uma verificação deve ser feita para
    evitar dados repetidos.
    '''

    def addTransition(self, transition):
        """
        :type transition: PNetTransition
        """

        self.listT[transition.node.id] = transition

    '''
    Os arcos ficam salvos numa lista com varios dicionários. Cada elemento da lista possui um dicionário
    com os mesmos cabeçalhos, mas com valores diferentes. Futuramente, uma verificação deve ser feita para
    evitar dados repetidos.
    '''

    def addArc(self, arc):
        """
        :type arc: PNetArc
        """

        self.listA.append(arc)

    def addTypes(self, types):
        self.listTy.append(types)

    def __str__(self):
        text = '--- Net:\nTypes:\n'
        for mode in self.listTy:
            text += str(mode.label.text) + '\n'
        text += '\nTransitions:\n'
        for transition in self.listT:
            text += str(transition) + '\n'
        text += '\nPlaces:\n'
        for place in self.listP:
            text += str(place) + '\n'
        text += '\nArcos:\n'
        for edge in self.listA:
            text += str(edge) + '\n'
        text += '---'

        return text
