import sys
import os
def count_def():
	cont = 0
	module_file = open('./Modules.py', 'r')
	list_line = module_file.readlines()
	for line in list_line:
		if (line.startswith('\tdef') == True):
			cont = cont + 1
	return cont

param = sys.argv[1:]
contador = 0
arq = open('./params.txt', 'w')
for method in param:
	contador = contador + 1
	if ( len(param) <= (count_def() - 1)):
		if (contador >= 1):
			line_arq = arq.write(str(method) + '\n')
	else:
		raise ("Numero de parametros errado")
arq.close()

os.system('scp ./params.txt pi@192.168.0.1:/home/pi')
