import sys  # argv for test file path

from br.icomp.ufam.parse.ParsePetriNet import ParsePetriNet
from br.icomp.ufam.util.Matrix import Matrix
from br.icomp.ufam.util.PNetExe import PNetExe
from br.icomp.ufam.util.ParserGabarito import parseLog

# TESTE DE PARSER
log = sys.argv[1]
gab = sys.argv[2]
n_q = sys.argv[3]
answers_list = parseLog(str(gab))
net = ParsePetriNet().parse_csv_file(str(log), answers_list)

print(net)

matrix = Matrix(net)
matrix.setMatrixI()
matrix.setMatrixO()
matrix.setMatrixD()
print(matrix)

exe = PNetExe(matrix, int(n_q))
exe.initMark()
print(exe)
exe.calculation()
print(exe)
