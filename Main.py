import argparse
import sys  # argv for test file path
from br.icomp.ufam.util.Matrix import Matrix
from br.icomp.ufam.parse.ParsePetriNet import ParsePetriNet


# TESTE DE PARSER
param = sys.argv[1]
net = ParsePetriNet().parse_csv_file(str(param))

print(net)

matrix = Matrix(net)
matrix.setMatrixI()
matrix.setMatrixO()
matrix.setMatrixD()
print(matrix)
