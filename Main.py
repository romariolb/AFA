from br.icomp.ufam.parse.Parse import ParsePetriNet
from br.icomp.ufam.util.Matrix import Matrix

# TESTE DE PARSER

obj = ParsePetriNet()
net = obj.parse_csv_file('Support/log-igorlucas-simulado2.CSV')

print(net)

"""matrix = Matrix(net)
matrix.setMatrixI()
matrix.setMatrixO()
matrix.setMatrixD()
print(matrix)
"""