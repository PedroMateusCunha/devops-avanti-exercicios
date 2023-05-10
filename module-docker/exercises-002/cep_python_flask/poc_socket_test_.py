#!/bin/usr/python3
""" Based in
    - https://realpython.com/python-sockets/
    - https://realpython.com/intro-to-python-threading/
"""

import threading
import socket
import requests

HOST = '127.0.0.1'
PORT = 5000

def socket_function_to_receive_connections(host: str, port: int):
    """ Function to run inside thread """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as new_socket:
        new_socket.bind((host, port))
        new_socket.listen()
        conn, addr = new_socket.accept()
        with conn:
            data_recv = conn.recv(1024)
            print('-----thread socket-------')
            print(data_recv)
            print('-------------------------')
            data_sent = (f'HTTP/1.1 200 ok\r\n'
                         f'Host: {HOST}:{PORT}\r\n'
                         f'Server: Python/Socket\r\n\r\n'
                         f'data sent to client\r\n\r\n')
            conn.sendall(bytes(data_sent, 'utf-8'))

thread_server_socket = threading.Thread(target=socket_function_to_receive_connections,
                                       args=(HOST, PORT))
thread_server_socket.start()

response_quest = requests.get(f'http://{HOST}:{PORT}/test', timeout=5)
print('========= request =======')
print(response_quest.text)
print(response_quest.status_code)
print('=========================')

thread_server_socket.join()
print('++++++++ FIM +++++++++')
