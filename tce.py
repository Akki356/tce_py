#!/usr/bin/env python2
from Crypto.Cipher import AES
import os
import sys
#i=raw_input()
os.system("cd "+sys.argv[1])
os.system("ls")
os.system("split -n "+sys.argv[2]+" "+sys.argv[1]+" "+sys.argv[1])
