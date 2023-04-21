#!/usr/bin/python
# coding: utf-8

from socket import *

def main():
    SERVER_PORT = 12000

    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', SERVER_PORT))

    print 'Servidor escutando na porta', SERVER_PORT
    print 'Aguardando pacotes...'

    try:
        while True:
            message, client_address = server_socket.recvfrom(2048)
            answer = message.upper()
            server_socket.sendto(answer, client_address)

            print 'Pacote recebido de', client_address

    except KeyboardInterrupt:
        server_socket.close()

        print 'Servidor encerrado.'


if __name__ == '__main__':
    main()
