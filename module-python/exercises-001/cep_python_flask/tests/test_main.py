#!/bin/usr/python3
""" Tests utils/loadinfo.py module
"""

import sys, os, threading, socket, time
up_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(up_directory)
import main
import utils.loadinfo
import testresources

environment_vars = utils.loadinfo.environment_vars()

def test__root_server__properties():
    function_result = main.root_server()
    assert type(function_result) is tuple
    assert len(function_result) == 2
    assert type(function_result[0]) is str
    assert len(function_result[0]) >= 300
    assert type(function_result[1]) is int
    assert function_result[1] >= 100 and function_result[1] < 600

def test__root_server__load():
    function_result = main.root_server()
    assert function_result[0].find('/quest') >= 0
    assert function_result[0].find('/list_csv') >= 0
    assert function_result[0].find('/list_html') >= 0
    assert function_result[0].find('/search_csv') >= 0
    assert function_result[0].find('/search_html') >= 0
    assert function_result[0].find('<h1>') >= 0
    assert function_result[0].find('function') == -1
    assert function_result[0].find('erro') == -1
    assert function_result[0].find('ERRO') == -1
    assert function_result[0].find('WARN') == -1
    assert function_result[0].find('warn') == -1

def test__quest_postal_code__properties_load():
    host = environment_vars["quest_container_name"]
    port = int(environment_vars["quest_container_port"])
    data_received = ''
    data_sent = (f'HTTP/1.1 200 ok\r\n'
                 f'Host: {host}:{port}\r\n'
                 f'Server: Python/Socket\r\n\r\n'
                 f'data sent to client')
    def mock_quest_socket(host: str, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data_received = conn.recv(1024)
                conn.sendall(bytes(data_sent, 'utf-8'))
    thread_server_socket = threading.Thread(target=mock_quest_socket,
                                            args=(host, port))
    thread_server_socket.start()
    function_result = main.quest_postal_code('02739000')
    # time.sleep(60) # needed to reuse same port in next test
    assert type(function_result) is tuple
    assert len(function_result) is 2
    assert function_result[0] == 'data sent to client'
    assert function_result[1] == 200

def test__list_csv__properties_load():
    host = environment_vars["list_csv_container_name"]
    port = int(environment_vars["list_csv_container_port"])
    data_received = ''
    data_sent = (f'HTTP/1.1 200 ok\r\n'
                 f'Host: {host}:{port}\r\n'
                 f'Server: Python/Socket\r\n\r\n'
                 f'data sent to client')
    def mock_quest_socket(host: str, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data_received = conn.recv(1024)
                conn.sendall(bytes(data_sent, 'utf-8'))
    thread_server_socket = threading.Thread(target=mock_quest_socket,
                                            args=(host, port))
    thread_server_socket.start()
    function_result = main.list_csv()
    # time.sleep(60) # needed to reuse same port in next test
    assert type(function_result) is tuple
    assert len(function_result) is 2
    assert function_result[0] == 'data sent to client'
    assert function_result[1] == 200

def test__list_html__properties_load():
    host = environment_vars["list_html_container_name"]
    port = int(environment_vars["list_html_container_port"])
    data_received = ''
    data_sent = (f'HTTP/1.1 200 ok\r\n'
                 f'Host: {host}:{port}\r\n'
                 f'Server: Python/Socket\r\n\r\n'
                 f'data sent to client')
    def mock_quest_socket(host: str, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data_received = conn.recv(1024)
                conn.sendall(bytes(data_sent, 'utf-8'))
    thread_server_socket = threading.Thread(target=mock_quest_socket,
                                            args=(host, port))
    thread_server_socket.start()
    function_result = main.list_html()
    # time.sleep(60) # needed to reuse same port in next test
    assert type(function_result) is tuple
    assert len(function_result) is 2
    assert function_result[0] == 'data sent to client'
    assert function_result[1] == 200
