#!/usr/bin/python3.9
# Encoding: utf-8
import os
try:
  import bcrypt,sys
except:
  os.system('pip install bcrypt')
  
if len(sys.argv) != 3:
  print("""
[{}] ----------------
[{}]   Bcrypt BruteForcer
[{}]  by: EtcAug10
[{}] ----------------

  USAGE:
    python bcrypt-bf.py [HASHED] [WORDLIST]
  EXAMPLE:
    python bcrypt-bf.py '$2y$12$QgdJPydR51XAU9Xi.iSSo.kj5mQ.8rvDShwJIHy.vNpH1mkmbgNwC' pass.txt

Happy Hacking <3
  """)
  exit()
else:
  encrypt = sys.argv[1]
  ls = open(sys.argv[2],'r').read().splitlines()
  try:
    print('Your encrypted string:\033[32;1m',encrypt)
    print('\033[00;0mYour plaintext:\033[32;1m',sys.argv[2])
    print("\033[00;0m\n\n[ RESULT ] :")
    for wl in ls:
      if bcrypt.checkpw(wl.encode(),bytes(encrypt.encode())):
        print("Found:",wl)
        break
      else:
        continue
    print("Huh.. It's done :D")
  except ValueError as er:
    print('\033[31;1m',er,'. \033[00;0mYour input string should be like this: \'ENCRYPT\' or this: "ENCRYPT"')
    print('It raise \'cause the value of $')
    
 #End of code <3