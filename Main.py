from br.icomp.ufam.parse.Parse import ParsePetriNet
from br.icomp.ufam.util.Matrix import Matrix

# TESTE DE PARSER

obj = ParsePetriNet()
obj.parse_csv_file('Support/2017139440220.csv')
nets = obj.parse_pnml_file('Support/Score_1_1.pnml')

print(obj)

for net in nets:
    matrix = Matrix(net)
    matrix.setMatrixI()
    matrix.setMatrixO()
    matrix.setMatrixD()
    print(matrix)
