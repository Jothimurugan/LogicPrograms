from pyVim import connect
import atexit
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.Datacenter], True)
print(obj_view)
Datacenters = obj_view.view
print(Datacenters)
obj = {}
for dc_name in Datacenters:
    print(dc_name.name)

atexit.register(connect.Disconnect, s_conn)