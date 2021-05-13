# Weather-box-light2
Taking data from pt100, dht22, SEN-14209 radiation sensor and sendig them through a client (utp) to a server 

Client.14.5 is the new one using threading in order to be more time efficient as the figure one depicts (the functions have different time complexity)


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
    
    
