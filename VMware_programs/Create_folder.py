from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

folder = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.Folder], True)
print(folder)

folders = folder.view
print(folders)

for f_name in folders:
    print(f_name.name)
    print(type(f_name))

new_folder = folders[0].CreateFolder(name = "DC_001")
print(new_dc.name)