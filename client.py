import socket
import time
from os import system, name
from colorama import init, Fore, Style

#TODO: port to flask
init(convert=True)

def clear():
    system('cls') if name == 'nt' else system('clear')

clear()

try:
    while True:
        print("Name?")
        namec = input("> ")
        if len(namec) >= 20:
            print(Fore.RED + "[ERROR] Your name needs to be less than 20 characters" +Style.RESET_ALL)
        else:
            break

    clear()

    host, port = ('localhost', 5656)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(Fore.LIGHTCYAN_EX + "[INFO] " +Style.RESET_ALL+ "Connection...")
    socket.connect((host, port))

    print(Fore.LIGHTCYAN_EX + "[INFO]"+Style.RESET_ALL+" Connected as "+ Fore.GREEN +namec+ Style.RESET_ALL)
    namec = namec.encode('utf8')
    socket.sendall(namec)

    while True:
        try:
            data = input("> ")
            #TODO: Permettre de recevoir les données pour pouvoir communiquer entre clients
            data = "("+Fore.LIGHTWHITE_EX+str(namec.decode())+Style.RESET_ALL+"): " + data
            data = data.encode('utf8')
            socket.sendall(data) 
        except ConnectionResetError:
            print(Fore.LIGHTRED_EX + "[ERROR] Connection reset. Is the server online?")
            time.sleep(5)
            break     
except ConnectionRefusedError:
    print(Fore.LIGHTRED_EX + "[ERROR] Connexion refused")
    time.sleep(5)
except ConnectionError:
    print(Fore.LIGHTRED_EX + "[Error] An error occured")
    time.sleep(5)
except ConnectionResetError:
    print(Fore.LIGHTRED_EX + "[ERROR] Connection reset. Is the server online?")
    time.sleep(5)
except KeyboardInterrupt:
    print(Fore.LIGHTRED_EX + "\nStopped!")
    time.sleep(5)
finally:
    socket.close()
