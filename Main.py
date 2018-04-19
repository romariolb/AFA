from br.icomp.ufam.parse.Parse import ParsePetriNet
from br.icomp.ufam.util.Matrix import Matrix

# TESTE DE PARSER

nets = ParsePetriNet().parse_pnml_file('Score_1_1.pnml')

for net in nets:
    print(net)
    matrix = Matrix(net)
    matrix.setMatrixI()
    matrix.setMatrixO()
    matrix.setMatrixD()
    print(matrix)
