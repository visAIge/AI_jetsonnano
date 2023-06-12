# -*- coding: utf-8 -*-
import subprocess
import os
import time
import shlex
import sys
from signal import signal, SIGPIPE, SIG_DFL



#cmd = 'python3 detect.py'
#proc = subprocess.Popen(shlex.split(cmd), stdout = subprocess.PIPE, shell=False)

if __name__=="__main__":

    print("Init")
    proc = subprocess.Popen([sys.executable,'-u','detect.py'], stdout=subprocess.PIPE, shell=False, universal_newlines=True)
    print(proc.pid)
    
    out = proc.stdout.readline()
    print(out)

    if "detectshoes" in out:
        print("Next Program")
        time.sleep(3)
        proc.terminate()

        time.sleep(5)
        proc_face = subprocess.Popen([sys.executable,'-u','ex.py'], stdout=subprocess.PIPE, shell=False, universal_newlines=True)
        print(proc.pid)

        out_f = proc_face.stdout.readline()
        print(out_f)

        if "RecognitionFace" in out_f:
            print("End")
            time.sleep(3)
            proc.terminate()
            signal(SIGPIPE, SIG_DFL)
