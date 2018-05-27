""" This program implements a parser and data structure for Petri net files.

This program implements an XML parser and a python data structure for
Petri nets/PNML created with VipTool or MoPeBs.
"""

import sys  # argv for test file path
import csv
import xml.etree.ElementTree as ET  # XML parser
from br.icomp.ufam.petrinet.PNet import PNet
from br.icomp.ufam.petrinet.PNetPlace import PNetPlace
from br.icomp.ufam.petrinet.PNetTransition import PNetTransition
from br.icomp.ufam.petrinet.PNetArc import PNetArc
from br.icomp.ufam.petrinet.PNetType import PNetType


class ParsePetriNet:
    """ This class represents a Petri net.

    This class represents a Petri net. A Petri net consists of
    a set of labelled labelled transitions, labelled places and
    arcs from places to transitions or transitions to places.

    net.edges: List of all edges of this Petri net
    net.transitions: Map of (id, transition) of all transisions of this Petri net
    net.places: Map of (id, place) of all places of this Petri net
    """

    def __init__(self):
        self.net = ''
        self.edges = []  # List or arcs
        self.transitions = {}  # Map of transitions. Key: transition id, Value: event
        self.places = {}  # Map of places. Key: place id, Value: place
        self.types = []  # List of data type from net.
        self.mark = []  # List of initial marks

    def __str__(self):

        text = '--- Net:\nTypes:\n'
        for mode in self.net.listTy:
            text += str(mode.label.text) + '\n'
        text += '\nTransitions:\n'
        for transition in self.net.listT:
            text += str(transition) + '\n'
        text += '\nPlaces:\n'
        for place in self.net.listP:
            text += str(place) + '\n'
        text += '\nArcos:\n'
        for edge in self.net.listA:
            text += str(edge) + '\n'
        text += '\nMarcação Inicial\n['
        for item in self.mark:
            text += str(item) + ' '
        text += ']\n---'

        return text

    def parse_csv_file(self, file):
        with open('Support/log-igorlucas-simulado2.CSV', 'r') as log:
            reader = csv.reader(log)
        for linha in reader:
            """
            Leitura dos componentes do .csv para atribuição aos objetos
            """
            ALUNO = linha[2]
            TEMPO = linha[3]
            foco = linha[6]
            tmp = foco.split(':')
            QUESTAO = str(tmp[0] + tmp[1])
            DIFC = str(tmp[2])
            RESPOSTA = QUESTAO + str(tmp[4])
            tmp2 = tmp[3].split('-')
            DISCIPLINA = str(tmp2[0])
            TOPICO = str(tmp2[1])

            """
            criação dos objetos de lugares, transições e arcos
            """

            placeQ = PNetPlace(QUESTAO, QUESTAO, DISCIPLINA, TOPICO, DIFC, TEMPO)
            placeR = PNetPlace(RESPOSTA, RESPOSTA, None, None, None, TEMPO)

            """
            Aqui precisa de uma rotina para contar quantas vezes eu estou passando
            pelo mesmo lugar.
            """

            transition1, transition2 = PNetTransition()

            









    def parse_pnml_file(self, file):
        """ This method parse all Petri nets of the given file.

        This method expects a path to a VipTool pnml file which
        represent a Petri net (.pnml), parse all Petri nets
        from the file and returns the Petri nets as list of PetriNet
        objects.

        XML format:
        <pnml>
          <net id="...">
            (<page>)
            <name>
              <text>name of Petri net</text>
            </name>
            <transition id="...">
              <name>
                <text>label of transition</text>
                <graphics>
                  <offset x="0" y="0"/>
                </graphics>
              </name>
              <graphics>
                <position x="73" y="149"/>
              </graphics>
            </transition>
            ...
            <place id="...">
              <name>
                <text>label of transition</text>
                <graphics>
                  <offset x="0" y="0"/>
                </graphics>
              </name>
              <graphics>
                <position x="73" y="149"/>
              </graphics>
              <initialMarking>
                <text>1</text>
              </initialMarking>
            </place>
            ...
            <arc id="..." source="id of source event" target="id of target event">
              <inscription>
                <text>1</text>
              </inscription>
            </arc>
            ...
            (</page>)
          </net>
          ...
        </pnml>
        """
        tree = ET.parse(file)  # parse XML with ElementTree
        root = tree.getroot()

        nets = []  # list for parsed PetriNet objects

        for net_node in root.iter('net'):
            # create PetriNet object
            self.net = PNet(net_node.get(id))
            nets.append(self.net)
            # net.name = net_node.find('./name/text').text

            # and data types
            for mode_type in net_node.iter('declaration'):
                mode = PNetType()
                mode.label = mode_type.find('./type/name')

                self.net.addTypes(mode)

            # and parse transitions
            for transition_node in net_node.iter('transition'):
                ID = transition_node.get('id')
                LABEL = transition_node.find('./name/text').text
                CODE = transition_node.find('./toolspecific/code/text').text
                GUARD = transition_node.find('./guard/text').text

                transition = PNetTransition(ID, LABEL, GUARD, CODE)
                self.net.addTransition(transition)

            # and parse places
            for place_node in net_node.iter('place'):
                ID = place_node.get('id')
                LABEL = place_node.find('./name/text').text
                TYPE = place_node.find('./type/text').text
                MARKING = place_node.find('./initialMarking/text').text

                place = PNetPlace(ID, LABEL, TYPE, MARKING)
                self.net.addPlace(place)

            # and arcs
            for arc_node in net_node.iter('arc'):
                ID = arc_node.get('id')
                SOURCE = arc_node.get('source')
                TARGET = arc_node.get('target')
                INSCRIPTION = arc_node.find('./inscription/text').text
                NET = self.net

                edge = PNetArc(ID, SOURCE, TARGET, INSCRIPTION, NET)
                self.net.addArc(edge)

        return nets

    def parse_csv_file(self, file):
        input_file = open(file)
        reader = csv.reader(input_file, delimiter=';')

        for linha in reader:
            resposta = linha[8]
            self.mark.append(resposta)
        input_file.close()
