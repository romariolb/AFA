import re

arquivo1 = open('Score_1.pnml','r')
arquivo2 = open('Score_1_1.pnml','w')

txt = arquivo1.readlines()

for linha in txt:
    n_str1 = re.sub('pnml:','',linha)
    n_str2 = re.sub('cpn:','',n_str1)
    arquivo2.writelines(n_str2)

arquivo1.close()
arquivo2.close()