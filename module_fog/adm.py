#Authors:Roberto Pacheco
#Universidade do Estado do Rio de Janeiro
#Departamento de Eletronica e Telecomunicacoes (DETEL)
#Project: SensingBus
#Subject: Send the preprocessing module to the Fog by SSH protocol. 

import os
import sys

params = sys.argv[1] #receive a parameter from the terminal 

os.system("mv ./%s.py manager_fog.py" %(params)) #rename the file to parameter name for manager_fog.py. 

os.system("scp ./manager_fog.py pi@192.168.0.1:/home/pi/") #send it to fog by ssh protocol

os.system("mv ./manager_fog.py %s.py" %(params)) #rename again to the original name
