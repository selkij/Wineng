import socket
import threading
import time
import sys
from os import system, name
from colorama import init, Fore, Style

init()

class ThreadClient(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    def run(self):
        while True:
            try:
                data = self.conn.recv(1024)
                data = data.decode('utf8')
                print(data)
            except OSError:
                pass
            except ConnectionAbortedError:
                pass
            except ConnectionResetError:
                # ! console spamming when client disconnect
                print(Fore.CYAN + "[INFO] "+Fore.RED+namec+Style.RESET_ALL+" disconnected")


class ConsoleThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # ! input not working when nobody connected at the start
        def my_input(prompt=''):
            print(prompt, end='', flush =True)
            for line in sys.stdin:
                if '\n' in line:
                    break
            return line.rstrip('\n')

        while True:
            inp = my_input()
            if inp == "exit":
                Commands.cexit()
            elif inp == "info":
                Commands.info()
            elif inp == "help":
                Commands.help()
            else:
                print(Fore.LIGHTWHITE_EX + "<"+Style.RESET_ALL+inp+Fore.LIGHTWHITE_EX+"> unknown, please type 'help' to see the list of available commands." +Style.RESET_ALL)


class Commands():
    def kick(cli=''):
        pass

    def info():
        print(Fore.LIGHTWHITE_EX+"Wineng Server Alpha 0.1, type 'help' for the list of commands"+Style.RESET_ALL)
    
    def cexit():
        # ! command really breaking everything (High Priority)
        try:
            print(Fore.LIGHTYELLOW_EX + "[WARNING] The connections to the server will get aborted, are you sure? [y] yes / [n] no (default [y])"+Style.RESET_ALL)
            choice = input("> ")
            if choice == "y":
                pass
            elif choice == "n":
                return
            conn.shutdown(2)
            conn.close()
            socket.close()
            sys.exit()
        except ConnectionAbortedError:
            pass

    
    def help():
        print(Fore.LIGHTGREEN_EX+ "[HELP]" +Style.RESET_ALL+ " The commands are: 'info' 'exit' 'help'")

    def clear():
        system('cls') if name == 'nt' else system('clear')

host, port = ('', 5656)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Commands.clear()

    print(Fore.LIGHTCYAN_EX + "[INFO]"+Style.RESET_ALL+" Server starting." +Style.RESET_ALL)
    socket.bind((host, port))
    print(Fore.LIGHTCYAN_EX + "[INFO]"+Style.RESET_ALL+" Server "+Fore.LIGHTGREEN_EX+"started"+Style.RESET_ALL)
except OSError:
    print(Fore.LIGHTRED_EX + "[ERROR] An error occurred. Maybe the server is already started?")
    time.sleep(5)
    sys.exit()

while True:

    try:
        socket.listen(5)
        conn, address = socket.accept()
        namec = conn.recv(1024)
        namec = namec.decode('utf8')
    except BufferError:
        print(Fore.LIGHTRED_EX + "[ERROR] A buffer error occurred" + Style.RESET_ALL)
        time.sleep(5)
    except OSError:
        pass
    except KeyboardInterrupt:
        Commands.Cexit()
        print(Fore.LIGHTCYAN_EX + "[INFO]" + Style.RESET_ALL + "server" + Fore.RED + "stopped" + Style.RESET_ALL)
        time.sleep(5)
        exit()

    print(Fore.LIGHTCYAN_EX + "[INFO] " +Fore.GREEN +namec+ Style.RESET_ALL + " connected")
    threadClient = ThreadClient(conn)
    threadClient.name = 'Client:' + namec
    threadClient.start()
    consoleThread = ConsoleThread()
    consoleThread.name = 'ConsoleThread'
    consoleThread.start()    

conn.close()
socket.close()  