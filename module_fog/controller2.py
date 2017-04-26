import sys
import Modules

def count_def():
	cont = 0
	module_file = open('./Modules.py', 'r')
	list_line = module_file.readlines()
	for line in list_line:
		if (line.startswith('\tdef') == True):
			cont = cont + 1
	return cont
	
def controller(postvars):
	module = Modules.Module(postvars)
	arquivo = open('./params.txt', 'r')
	line_file = arquivo.readlines()
	for line in line_file:
		if (line == "delete_data\n"):
			module.delete_data()
		elif (line == "media_measure\n"):
			print 'oi'
			#media_measure = module.media_measure(measure)
		else:
			pass










			
	
