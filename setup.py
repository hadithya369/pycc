import os
from cryptography.fernet import Fernet
try:
    f1=open('pycc-config.co','r')
    t1=[]
    for t in f1:
        t1.append(t)
    f1.close()

    cppfile1=t1[0]
    objfile1=t1[1]
    f2n1=t1[2]
    f3n1=t1[3]
except Exception as Ex:
    print('Corrupted or no config file pycc-config.co\n Enter all details to recreate file (Don\'t leave empty )')
cppfile=input('C++ Filename : ')
objfile=input('Object Filename (Leave Empty to keep it unchanged) : ')
f2n=input('Output Filename (Leave Empty to keep it unchanged) : ')
f3n=input('Expected Output Filename (Leave Empty to keep it unchanged) : ')

f1=open('pycc-config.co','wb')
key=Fernet.generate_key()
f=Fernet(key)
f1.write(key)
f1.write(bytes('\n','utf-8'))
f1.write(f.encrypt(bytes(cppfile,'utf-8')))
f1.write(bytes('\n','utf-8'))
if objfile!='':
    objfile1=objfile
if f2n!='':
    f2n1=f2n
if f3n!='':
    f3n1=f3n
f1.write(f.encrypt(bytes(objfile,'utf-8')))
f1.write(bytes('\n','utf-8'))
f1.write(f.encrypt(bytes(f2n,'utf-8')))
f1.write(bytes('\n','utf-8'))
f1.write(f.encrypt(bytes(f3n,'utf-8')))
f1.write(bytes('\n','utf-8'))

f1.close()