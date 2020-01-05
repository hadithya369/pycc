import re
from itertools import zip_longest

def is_cpp(fn):
    return re.search('.*{1}\.cpp',fn)

def cl_line(ltc):
    ltc=re.split('[ \n]',ltc)
    tltc=[]
    for el in ltc:
        if el!='':
            tltc.append(el)
    return tltc

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
    for e1,e2 in zip_longest(e11,e22):
        if(e1 is None or e2 is None):
            fl=False
        if(fl==False or e1[0]!=e2[0]):
            print('\n\nToken Test Failed\n\n')
            if(fl!=False):
                print('Line : '+str(e2[1]))
                print('Expected : ....'+str(e1[0])+'....')
                print('Found : ....'+str(e2[0])+'....')
            return
    print('\n\nPassed All Test Cases\n\n')
    f1.close()
    f2.close()

def stcmp(f1name,f2name): #Strict test tests if 2 files are identical
    f1=open(f1name,'r')
    f2=open(f2name,'r')
    line=0
    fl=True
    for e1,e2 in zip_longest(f1,f2) :
        if(e1 is None or e2 is None):
            fl=False
        if(fl==False or e1!=e2):
            print('Strict Test Failed')
            print('Line : '+str(line))
            print('Expected : ....'+str(e1)+'....')
            print('Found : ....'+str(e2)+'....')
            line=-1
            break
        line=line+1
    if line!=-1:
        print('Strict Test Successful')
    f1.close()
    f2.close()