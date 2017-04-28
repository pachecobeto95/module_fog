# Module's Fog

Os arquivos fog_agent_new_test.py, Modules.py, controller2.py ficam na Fog. 

O fog_agent_fog_new_test.py faz o mesmo qu o fog_agent.py do repositorio do 
SensingBus. A cada mensagem recebida, esse script executa função do controller 
do arquivo controller2.py.
A funcao controller le os as linhas do do arquivo "params.txt".
Lendo esse arquivo, assim que lê uma das funções de processamento que a fog
deve executar. Essa funcao chama o esse modulo de processamento no script
Modules.py

No computador do administrador ficará os arquivos user.py e script_example.py.
Este executa um script de escrever em um arquivo "params.txt" um parametro
informado pelo shell script no terminal na hora de executar o script_example.py
Aquele script, user.py, faz o mesmo procedimento pelo python. Pensei em fazer
por shell script pq queria que menos o adm tivesse acesso a codigo ou algo assim

Outra opção que pensei foi o adm executar um script que funcionaria como
um cliente que mandaria um dado para a fog. Esse dado seria a função do modulo
de processamento a ser importada e executada pela fog.

Mas esse metodo seria igual a criar um caminho reverso, entao achei que nao
era o requisitado, apesar de pessoalmente achar mais elegante.

Outro metodo trata-se de execução de script de cliente executado pelo adm 
do sistema para enviar uma mensagem a Fog. Aproveitando o fato que a Fog ja ta
funcionando como servidor recebendo mensagens. Essa mensagem contem outro type. 
Assim que identifica o type "cloud" no corpo da mensagem. A fog procura outros parametros 
no corpo da mensagem pra executar o modulo ordenado. O adm do sistema entra com os dados 
de qual modulo de processamento atraves de parametros na execuçao do codigo cliente.

Fiz esse README.md correndo. Vou comentar os arquivos ainda
