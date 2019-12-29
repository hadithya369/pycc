import os
import re
import sys
import subprocess
from cryptography.fernet import Fernet

def cl_line(ltc):
    ltc=re.split('[ \n]',ltc)
    tltc=[]
    for el in ltc:
        if el!='':
            tltc.append(el)
    return tltc

def readdata():
    f1=open('pycc-config.co','rb')
    t1=[]
    for el in f1:
        el=el[:-1]
        t1.append(el)
    key=t1[0]
    f=Fernet(key)
    cppfile=f.decrypt(t1[1]).decode('utf-8')
    objfile=f.decrypt(t1[2]).decode('utf-8')
    f2n=f.decrypt(t1[3]).decode('utf-8')
    f3n=f.decrypt(t1[4]).decode('utf-8')
    return [cppfile,objfile,f2n,f3n]


def rcmp(f1name,f2name): #Token Test tests tokens separated by space or newline
    f1=open(f1name,'r')
    f2=open(f2name,'r')
    line=0
    e11=[]
    e22=[]
    for e1 in f1:
        line=line+1
        for el in cl_line(e1):
            e11.append([el,line])
    line=0
    for e2 in f2:
        line=line+1
        for el in cl_line(e2):
            e22.append([el,line])
    fl=True
    if(len(e11)!=len(e22)):
        fl=False
        print('\n\nToken Test Failed\n\n')
        return
    for e1,e2 in zip(e11,e22):
        if(e1[0]!=e2[0] or fl==False):
            print('\n\nToken Test Failed\n\n')
            print('Line : '+str(e2[1]))
            print('Expected : ....'+e1[0]+'....')
            print('Found : ....'+e2[0]+'....')
            return
    print('\n\nPassed All Test Cases\n\n')
    f1.close()
    f2.close()

def stcmp(f1name,f2name): #Strict test tests if 2 files are identical
    f1=open(f1name,'r')
    f2=open(f2name,'r')
    line=0
    for e1,e2 in zip(f1,f2) :
        if(e1!=e2):
            print('Strict Test Failed')
            print('Line : '+str(line))
            print('Expected : ....'+e1+'....')
            print('Found : ....'+e2+'....')
            line=-1
            break
        line=line+1
    if line!=-1:
        print('Strict Test Successful')
    f1.close()
    f2.close()

cppfile='tes.cpp'
objfile='a_obj'
f2n='a_output.txt'
f3n='a_eout.txt'
stbool=False
cppfile,objfile,f2n,f3n=readdata()
args=sys.argv
argl=len(args)
i=0

while i<argl:
    if(args[i]=='--cppfile'):
        i=i+1
        cppfile=args[i]
    if(args[i]=='--objfile'):
        i=i+1
        objfile=args[i]
    if(args[i]=='--ofile'):
        i=i+1
        f2n=args[i]
    if(args[i]=='--eofile'):
        i=i+1
        f3n=args[i]
    if(args[i]=='--s'):  #To perform strict test
        stbool=True
    i=i+1

compile_comm='g++ '+cppfile+' -o '+objfile
exec_comm=objfile
try:
    if not(os.path.exists(cppfile)):
        raise Exception('File not found : '+cppfile)
    if not(os.path.exists(f2n)):
        raise Exception('File not found : '+f2n)
    if not(os.path.exists(f3n)):
        raise Exception('File not found : '+f3n)
    subprocess.check_output(compile_comm)
    print('\n\nCompilation Successful\n\n')
    subprocess.call(exec_comm)
    print('\n\nExecution Successful\n\n')
    rcmp(f3n,f2n)
    if stbool==True:
        stcmp(f3n,f2n)
    aeiou=input('')
except Exception as Ex:
    print(Ex)
    print('Check your syntax or recreate the configuration file')


