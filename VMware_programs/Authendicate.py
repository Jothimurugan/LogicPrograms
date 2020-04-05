from pyVim.connect import SmartConnect, SmartConnectNoSSL
from pyVim import connect
import atexit

sconn = SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
print("Authendication Successfully")

atexit.register(connect.Disconnect, sconn)
print("Disconnected successfully")