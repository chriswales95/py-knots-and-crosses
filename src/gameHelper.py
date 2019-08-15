import os


def clearConsole():
    if(os.uname().sysname == 'Darwin'):
        os.system("clear")
    else:
        os.system("cls")
