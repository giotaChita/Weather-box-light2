# Weather-box-light2
Taking data from pt100, dht22, SEN-14209 radiation sensor and sendig them through a client (utp) to a server 

Client.py is the new one using threading in order to be more time efficient as the figure one depicts (the functions have different time complexity)


### LIBRARIES to download for rpi

### For pt100:

    pip3 install adafruit-circuitpython-ads1x15
   
    pip3 install adafruit-circuitpython-lis3dh
    
    pip3 install sympy
 ### For radiation sensor
    
    sudo apt-get install python3-rpi.gpio
    
    sudo pip3 install PiPocketGeiger
    
 ### For DHT22 sensor
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-dev python3-pip
    sudp python3 -m pip install --upgrade pip setuptools wheel
    sudo pip3 install Adafruit_DHT

run only on python3 

  >0x48 (1001000) ADR -> GND
  >
  >0x49 (1001001) ADR -> VDD
  >
  >0x4A (1001010) ADR -> SDA
  >
  >0x4B (1001011) ADR -> SCL
    
    ### MANUAL 
    1. make the connection between rpi and the sensor -> graphs and pins' connection in drive -> 06-electronics (from dht22 and radiation sensor)  
    2. connect rpi with the wifi and power up the rpi 
    3. open terminal or the app to run the python script  
    4. if you open the terminal donwnload the above libryries (if you have not already installed in our case they are installed)
    5a. run the programm from terminal  : python3 client.py
    5b. run the programm through -> open menu application -> Thonny Python IDE: just open the programm it will be saved in desktop in order to be found easily 
    6. then the client will be ready to be connected with the server
    7. run the server from you laptop though pycharm or whatever you want
    8. the data should be sent successfully
    9.a (terminal way) in order to stop the program press Ctr + C
    9.b just press stop to terminate the program 
