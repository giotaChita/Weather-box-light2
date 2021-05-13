import socket
import ipaddress
from all1 import*
import time
from datetime import datetime
import pickle
import sys
import pandas as pd
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import threading
import ctypes

PORT = 5005
SERVER = ipaddress.ip_address("192.168.1.3")
ADDR = (str(SERVER),PORT)

#creating the socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(ADDR) 

def send(msg):
        client.send(pickle.dumps(msg))

def send_radiation():
    times = list()
    with RadiationWatch(24, 23) as radiationWatch:
        start = timer()
        for _ in range(101):
            send(radiationWatch.status())
            time.sleep(0.5)
            times.append(timer()-start)
        plt.plot(times,label = "radiation")
        plt.xlabel("data_package")
        plt.ylabel("time(s)")
        plt.legend()
        plt.show()

def send_temp_dht22():
    times = list()
    start = timer()
    for _ in range(101):
        send(take_temp())
        times.append(timer()-start)
    plt.plot(times,label = "temp")
    plt.legend()
    plt.show()

def send_hum():
    #while 1:
    times = list()
    start = timer()
    for _ in range(101):
        send(take_hum())
        times.append(timer()-start)
    plt.plot(times,label = "humidity")
    plt.legend()
    plt.show()

def send_temp_pt100():
    #while 1:
    times = list()
    start = timer()
    for _ in range(101):
        send(temps())
        times.append(timer()-start)
    plt.plot(times,label = "pt100")
    plt.legend()
    plt.show()

rs = threading.Thread(target = send_radiation)
hs = threading.Thread(target = send_hum)
ts_dht22 = threading.Thread(target = send_temp_dht22)
ts_pt100 = threading.Thread(target = send_temp_pt100)

ts_pt100.start()
rs.start()
hs.start()
ts_dht22.start()

ts_pt100.join()
rs.join()
hs.join()
ts_dht22.join()


        