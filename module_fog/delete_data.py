#Authors:Roberto Pacheco
#Universidade do Estado do Rio de Janeiro
#Departamento de Eletronica e Telecomunicacoes (DETEL)
#Project: SensingBus: Pre-processing Module
#Subject: 

def cartridge(tmp): #delete the defective data, do the last line always empty 
	delete_list = []
	for i in range(len(tmp)):
		if (tmp[i][0:-1] == 0): #if the last line were empty, add it to delete_list list.
			delete_list.append(i)
	for i in reversed(delete_list):
		del tmp[i]

	return tmp

