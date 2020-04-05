from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.Datacenter], True)
print(obj_view)
f = obj_view.view

for datacenter in f:
    if datacenter.name == "newDC":
        datacenter.hostFolder.CreateFolder(name = "FolderinDC")