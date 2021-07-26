import socket
from colorama import init, Fore, Style

init(convert=True)

try:
    print("Name?")
    name = input("> ")

    host, port = ('localhost', 5656)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port))

    print("[INFO] Connected as "+ Fore.GREEN +name+ Style.RESET_ALL)
    name = name.encode('utf8')
    socket.sendall(name)

    while True:
        try:
            data = input("> ")

            if data == " ":
                pass
            else:
                data = "("+str(name.decode())+"): " + data
                data = data.encode('utf8')
                socket.sendall(data) 
        except ConnectionResetError:
            print("[ERROR] Connection reset. Is the server online?")
            break     
except ConnectionRefusedError:
    print(Fore.RED + "[ERROR] Connexion refused.")
except ConnectionError:
    print(Fore.RED + "[Error] An error occured.")
except ConnectionResetError:
    print(Fore.RED + "[ERROR] Connection reset. Is the server online?")
except KeyboardInterrupt:
    print(Fore.RED + "\nStopped!")
finally:
    socket.close()
