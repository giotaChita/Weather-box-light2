import socket
import ipaddress
from all1 import*
import time
from datetime import datetime
import pickle
import sys
import pandas as pd
#from humidity import take_data
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
HEADER = 64
PORT = 5051
FORMAT = 'utf-8'

DISCONNECT_MESSAGE = 'DISCONNECT'
SERVER = ipaddress.ip_address("192.168.0.104")
ADDR = (str(SERVER),PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(ADDR) # inerver -> bind

def send(msg):
    #message = msg.encode(FORMAT) #from string to bytes in order to send the msg
    #msg_length = len(message)
    #send_length = str(msg_length).encode(FORMAT)
    #i have to make sure that it is going to be 64
    # send_length += b' ' * (HEADER-len(send_length))
    #client.send(send_length)
    client.send(msg)
#send(str(take_data()))
#send(str(radiationWatch.status()))
     
#send(DISCONNECT_MESSAGE)


if __name__ == "__main__":
    # Create the RadiationWatch object, specifying the used GPIO pins ...
    with RadiationWatch(24, 23) as radiationWatch:        
        while 1:
            now = datetime.now()
            #print("Chris is trying to be funny")
            # ... and simply print readings each 1 seconds.
            dict1 = {"TEMP [*C]" : take_temp(),
                    "HUM [%]" : take_hum(),
                     "TIME": now.strftime("%H:%M:%S"),
                     "RADIATION [cmp]": radiationWatch.status()}
                     #"TEMP_OUT [*C]": temps()}
            #data = pickle.dumps(dict1, -1)
            #size = sys.getsizeof(data)
#            print(size)
 #           print(dict1)
           # send(data)
           # send(str(dict1))
           # dp = pd.DataFrame(dict1)
            #print(dp)
            df = pd.DataFrame(list(dict1.items()), columns = ['Column1','Column2'])
           #times = list()
            #for _ in range(10):
            #   start = timer()
             #   temps()
              #  times.append(timer()-start)
            #plt.plot(times, label = "pt100")
            #plt.legend()
            #plt.show()
            print(df)
            print("\t===========================")
            #send(dict1)

