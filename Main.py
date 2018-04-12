from br.icomp.ufam.parse.Parse import ParsePetriNet

# TESTE DE PARSER

o = ParsePetriNet()
nets = o.parse_pnml_file('Score_1_1.pnml')

for net in nets:
    print(net)
