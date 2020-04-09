from pyVim import connect
import atexit
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.HostSystem], True)

esxi_hosts = obj_view.view

for esxi_host in esxi_hosts:
    print(esxi_host.name)

atexit.register(connect.Disconnect, s_conn)

