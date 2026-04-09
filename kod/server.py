#==============================#
#                              #
#      Server Programmet       #
#                              #
#==============================#
# Oscar Hellgren Te23A Ebersteinska Gy


# Importer
from time import time
from threading import Thread
from socket import gethostname, gethostbyname, socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST
from ansi_colors import Colors



# Klasser/ansvar:

# En klass som ansvarar för att skriva ut meddelanden som alla andra klasser ärver
# Den ska skicka ut vanliga, varnings och error meddelanden.
# 2026/04/06

class ConsoleOutput(Colors):
    def __init__(self, id:str):
        self.id = id

    def standard(self, message: str):
        print(self.BLACK + "[" + "       " + "] ", end=self.end)
        print(self.bold + self.MAGENTA + "@" + self.id, end=self.end)
        print(self.BLACK + " -> ", end=self.end)
        print(message)


    def warning(self, message: str):
        print(self.BLACK + "[" + self.bold + self.YELLOW + "WARNING" + self.end + self.BLACK + "] ", end=self.end)
        print(self.bold + self.MAGENTA + "@" + self.id, end=self.end)
        print(self.BLACK + " -> ", end=self.end)
        print(message)

    def error(self, message: str):
        print(self.BLACK + "[" + self.bold + self.RED + " ERROR " + self.end + self.BLACK + "] ", end=self.end)
        print(self.bold + self.MAGENTA + "@" + self.id, end=self.end)
        print(self.BLACK + " -> ", end=self.end)
        print(message)



# En klass som ansvarar för all info om datorn e.g. hostname; ip; portar
# 2026/04/05
class ComputerInfo(ConsoleOutput):
    def __init__(self, port_udp: int = 8888, port_tcp: int = 5555):
        super.__init__("Computer info")

        self.name = gethostname()
        self.address = gethostbyname(self.name)
        self.udp_port = port_udp
        self.tcp_port = port_tcp




# En klass som ansvarar för udp anrop
# Som default bör den skrika datorns Hostname (Mitt fall "Marathon")
# Denna klass ska sälv ansvara för att skicka udp anrop men ska också ha en terminerings metod
# Egen mainloop som kan köras asyncront
# 2026/04/06
class UdpBroadcaster(ConsoleOutput):
    def __init__(self, message: str, target_ip: str, port: int, delay: float = 1):
        super.__init__("UDP broadcaster")

        self.message = message
        self.target = target_ip
        self.port = port
        self.delay = delay
        self.running = True

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        self.thread = Thread(None, self.mainloop)
        #self.thread.start()


    def mainloop(self):
        packed_binary = self.message.encode("UTF-8")
        destination = (self.target, self.port)
        pit = 0

        while self.running:
            if (time() - pit) >= self.delay:
                self.socket.sendto(packed_binary, destination)
                pit = time()


    
    def stop(self):
        self.running = False
        self.thread.join()
        self.socket.close()


out = ConsoleOutput("ConsoleOutput")

out.standard("Standard")
out.warning("Warning")
out.error("Error")