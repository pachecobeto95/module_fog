#Authors:Roberto Pacheco
#Universidade do Estado do Rio de Janeiro
#Departamento de Eletronica e Telecomunicacoes (DETEL)
#Project: SensingBus: Remote management of the pre-processing modules
#Subject: Interface to receive the pre-processing modules by SSH from the network administrator. 

import manager_fog
class module(object):

	def __init__ (self, tmp):
		self.tmp = tmp
		self.data = []

	def controller(self):
		self.data.append(manager_fog.cartridge(self.tmp))

	def get_payload(self):
		return self.data

		
