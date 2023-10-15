
import subprocess
import sys
from colorama import Fore,Style

banner=Fore.YELLOW+"""

 ▄▄▄       ███▄    █ ▓█████▄ ▓█████▄  ██▀███   ▒█████   ██▓▓█████▄  ██▀███   ██ ▄█▀ ██▓▄▄▄█████▓
▒████▄     ██ ▀█   █ ▒██▀ ██▌▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓██▒▒██▀ ██▌▓██ ▒ ██▒ ██▄█▒ ▓██▒▓  ██▒ ▓▒
▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒██▒░██   █▌▓██ ░▄█ ▒▓███▄░ ▒██▒▒ ▓██░ ▒░
░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌░▓█▄   ▌▒██▀▀█▄  ▒██   ██░░██░░▓█▄   ▌▒██▀▀█▄  ▓██ █▄ ░██░░ ▓██▓ ░ 
 ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░▒████▓ ░██▓ ▒██▒░ ████▓▒░░██░░▒████▓ ░██▓ ▒██▒▒██▒ █▄░██░  ▒██▒ ░ 
 ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▓   ▒▒▓  ▒ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░▓    ▒ ░░   
  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░  ▒ ░ ░ ▒  ▒   ░▒ ░ ▒░░ ░▒ ▒░ ▒ ░    ░    
  ░   ▒      ░   ░ ░  ░ ░  ░  ░ ░  ░   ░░   ░ ░ ░ ░ ▒   ▒ ░ ░ ░  ░   ░░   ░ ░ ░░ ░  ▒ ░  ░      
      ░  ░         ░    ░       ░       ░         ░ ░   ░     ░       ░     ░  ░    ░           
                      ░       ░                             ░                                   

"""
while True:
    subprocess.run("clear")
    print(banner)

    import sourcedefender


    print("\033[96m [0]\033[00m Build ")

    print("\033[96m [1]\033[00m Start listner")
    print()

    a=int(input("\033[96m Enter no :\033[00m "))
    if a==0:
        subprocess.run("clear")
        print(banner)
        import build
        print(" \033[92m[#]\033[00m Are you want to start listner? (yes/no) : ",end="")
        a=input()
        if a=="no":
            print(" \033[92m[#]\033[00m Exit. ",end="")
            sys.exit()
        else:
            import sourcedefender
            import Tkmulticlient
            break
    elif a==1:
        import sourcedefender
        import Tkmulticlient
        break