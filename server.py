import socket
import threading
import time
from colorama import init, Fore, Style

init(convert=True)

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
            except ConnectionResetError:
                print("[INFO] "+Fore.RED+name+Style.RESET_ALL+" disconnected")
                break


class ConsoleThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        while True:
            inp = input("> ")
            if inp == "/exit":
                Commands.Cexit()
            elif inp == "/info":
                Commands.info()


class Commands():
    def kick(cli):
        pass

    def info():
        print("Wineng Server Alpha 0.1, type '/help' for the list of commands")
    
    def Cexit(self):
        try:
            conn.close()
            #AttributeError: 'socket' object has no attribute 'SHUT_RDWR'
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except socket.error:
            pass
        except ConnectionAbortedError:
            print(Fore.YELLOW + "[WARNING] The connections to the server got aborted")
            print("[WARNING] The program will stop in 5 seconds..." + Style.RESET_ALL)
            time.sleep(5)
            exit()
        

host, port = ('', 5656)

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((host, port))
    print("[INFO] Server "+Fore.GREEN+"started"+Style.RESET_ALL)
except OSError:
    print(Fore.RED + "[ERROR] An error occured. Maybe the server is already started?")

while True:

    try:
        socket.listen(5)
        conn, address = socket.accept()
        name = conn.recv(1024)
        name = name.decode('utf8')
    except BufferError:
        print(Fore.RED + "[ERROR] A buffer error occured" + Style.RESET_ALL)
        break
    
    print("[INFO] " +Fore.GREEN +name+ Style.RESET_ALL + " connected")
    my_thread = ThreadClient(conn)
    my_thread.start()
    consoleThread = ConsoleThread()
    consoleThread.start()
    

conn.close()
socket.close()  
