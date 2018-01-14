#Authors:Roberto Pacheco
#Universidade do Estado do Rio de Janeiro
#Departamento de Eletronica e Telecomunicacoes (DETEL)
#Project: SensingBus
#Subject: Send the preprocessing module to the Fog by SSH protocol. 

import os
import sys

params = sys.argv[1]

os.system("mv ./%s.py manager_fog.py" %(params))

os.system("scp ./manager_fog.py pi@192.168.0.1:/home/pi/")

os.system("mv ./manager_fog.py %s.py" %(params))
