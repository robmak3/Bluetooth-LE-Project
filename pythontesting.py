import pydbus
import os
import time
import sys

bus = pydbus.SystemBus() #Opens the SystemBus API for us to read

IC4MacAddress = input("Your Phone Mac Address has not been saved. Please input your Phone Mac Address:")

try:
    aaa = '/org/bluez/hci0/dev_' + IC4MacAddress.replace(":", "_")
    device = bus.get('org.bluez', aaa)
    device.Connect()
except:
    print("connection failed, please make sure your mac adress is accurate, and that you ran with sudo -E")
    sys.exit()
print('Now Connected')

print("sleeping while discovering attributes")
time.sleep(10)

try:
    Handle = bus.get("org.bluez", aaa + '/service002f/char0030')

    a = Handle.AcquireNotify({})
except:
    print('failed to connect to attributes, make sure you are using the right app')

try:
    aa = os.fdopen(a[0], "r")
except: 
    print("failed to open file descriptor for bluez")
    device.Disconnect()

print("\nsleeping while getting notifications")
time.sleep(10)

os.lseek(a[0], 0, 0)
print(os.read(a[0], 100)) #read 100 characters

aa.close()
device.disconnect() #closes everything out
sys.exit()
