import argparse
import sys  # argv for test file path
from br.icomp.ufam.util.ParserGabarito import parseLog
from br.icomp.ufam.util.Matrix import Matrix
from br.icomp.ufam.parse.ParsePetriNet import ParsePetriNet


# TESTE DE PARSER
log = sys.argv[1]
gab = sys.argv[2]
gablist = parseLog(str(gab))
net = ParsePetriNet().parse_csv_file(str(log), gablist)

print(net)

matrix = Matrix(net)
matrix.setMatrixI()
matrix.setMatrixO()
matrix.setMatrixD()
print(matrix)
