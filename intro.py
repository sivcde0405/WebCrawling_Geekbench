import time
import platform
import psutil

def introprog():
    print('''
    ░██╗░░░░░░░██╗███████╗██████╗░░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░██╗███╗░░██╗░██████╗░
    ░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██║████╗░██║██╔════╝░
    ░╚██╗████╗██╔╝█████╗░░██████╦╝██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░██║██╔██╗██║██║░░██╗░
    ░░████╔═████║░██╔══╝░░██╔══██╗██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██║██║╚████║██║░░╚██╗
    ░░╚██╔╝░╚██╔╝░███████╗██████╦╝╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗██║██║░╚███║╚██████╔╝
    ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░

    ░██████╗░███████╗███████╗██╗░░██╗██████╗░███████╗███╗░░██╗░█████╗░██╗░░██╗  ██╗░░░██╗░░███╗░░░░░░█████╗░
    ██╔════╝░██╔════╝██╔════╝██║░██╔╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║░░██║  ██║░░░██║░████║░░░░░██╔══██╗
    ██║░░██╗░█████╗░░█████╗░░█████═╝░██████╦╝█████╗░░██╔██╗██║██║░░╚═╝███████║  ╚██╗░██╔╝██╔██║░░░░░██║░░██║
    ██║░░╚██╗██╔══╝░░██╔══╝░░██╔═██╗░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██╔══██║  ░╚████╔╝░╚═╝██║░░░░░██║░░██║
    ╚██████╔╝███████╗███████╗██║░╚██╗██████╦╝███████╗██║░╚███║╚█████╔╝██║░░██║  ░░╚██╔╝░░███████╗██╗╚█████╔╝
    ░╚═════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░╚════╝░
    ''')
    print('made by sivcde0405')
    time.sleep(5)

    mem = psutil.virtual_memory()
    print('\n---system info---')
    print('OS                   :\t', platform.system())
    print('OS Version           :\t', platform.version())
    print('Process information  :\t', platform.processor())
    print('Process Architecture :\t', platform.machine())
    print('RAM                  :\t %.4f GB' % (mem.total / 1024 ** 3))

    print('\n\n---now start---')
    time.sleep(0.5)
    print('now loading DB (0%)')
    time.sleep(0.5)