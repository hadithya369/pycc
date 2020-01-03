import os
from checks import rcmp,stcmp
import sys
import subprocess
from cryptography.fernet import Fernet
import getpass
import Browse as br
arg_list=sys.argv

def is_cpp(fn):
    return fn[-4:]=='.cpp'

def make_dir(dirname):
    exit_code=subprocess.call('mkdir '+dirname,shell=True)
    return exit_code

def change_cred():
    un=input('Enter Username: ')
    while(True):
        ps=getpass.getpass('Enter new password: ')
        ps2=getpass.getpass('Re-enter new password: ')
        if(ps!=ps2):
            print('Passwords dont match')
        else:
            break
    f1=open('F:\pycc-config.co','w')
    f1.write(un)
    f1.write('\n')
    f1.write(ps)

def get_user_cred():
    try:
        f1=open('F:\pycc-config.co','r')
    except Exception as Ex:
        change_cred()
        f1=open('F:\pycc-config.co','r')
    fd=[]
    for el in f1:
        fd.append(el)
    return fd

def check_input():
    if(arg_list[1]=='create'):
        if (len(arg_list)!=3):
            print('Check syntax\nUsage: pycc create problem_code')
            return
        exc=make_dir(arg_list[2])
        if(exc!=0):
            return
        os.chdir(arg_list[2])
        f1=open(arg_list[2]+'.cpp','w')
        f1.close()
        f1=open(arg_list[2]+'_i.txt','w')
        f1.close()
        f1=open(arg_list[2]+'_o.txt','w')
        f1.close()
        f1=open(arg_list[2]+'_e.txt','w')
        f1.close()
    elif(arg_list[1]=='run'):
        if(is_cpp(arg_list[2])==False):
            print('CPP files only')
        if not((len(arg_list)==4 and arg_list[3]=='-s') or len(arg_list)==3):
            print('Check syntax\nUsage: pycc run cppfile [-s]')
            return
        fl=len(arg_list)==4
        dirname=os.getcwd().split(os.path.sep)[-1]
        if not(os.path.exists(arg_list[2])):
            print('CPP file not found: '+arg_list[2])
            return
        if not(os.path.exists(dirname+'_i.txt')):
            print('Input file not found: '+dirname+'_i.txt')
            return
        if not(os.path.exists(dirname+'_o.txt')):
            print('Output file not found: '+dirname+'_o.txt')
            return
        if not(os.path.exists(dirname+'_e.txt')):
            print('Expexcted Output file not found: '+dirname+'_e.txt')
            return
        compile_comm='g++ '+arg_list[2]+' -o '+dirname
        exec_comm=dirname
        exit_code=subprocess.call(compile_comm)
        if(exit_code!=0):
            return
        print('\n\nCompilation Successful\n\n')
        exit_code=subprocess.call(exec_comm)
        if(exit_code!=0):
            return
        print('\n\nExecution Successful\n\n')
        rcmp(dirname+'_e.txt',dirname+'_o.txt')
        if fl==True:
            stcmp(dirname+'_e.txt',dirname+'_o.txt')
    elif(arg_list[1]=='submit'):
        if(is_cpp(arg_list[2])==False):
            print('CPP files only')
        if not((len(arg_list)==4 and arg_list[3]=='-c') or len(arg_list)==3):
            print('Check syntax\nUsage: pycc submit cppfile [-c]')
            return
        fl=len(arg_list)==4
        if(fl==True):
            change_cred()
        if not(os.path.exists(arg_list[2])):
            print('CPP file not found: '+arg_list[2])
            return
        if get_user_cred()==None or len(get_user_cred())!=2:
            change_cred()
        us,ps=get_user_cred()
        cn=input('Contest Name(Leave Empty if submission is not to an ongoing contest): ')
        prco=input('Problem code: ')
        res=br.submit_solution(us,ps,prco,arg_list[2],cn)
        print(res)


    else:
        print('Check Syntax\nUsage: pycc [command] [filename] [-s -c]')


check_input()