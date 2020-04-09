from pyVim import connect
import atexit
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()
# print(contents)

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.HostSystem], True)
print(obj_view)
esxi_hosts = obj_view.view
print(esxi_hosts)

for esxi_host in esxi_hosts:
    print(esxi_host.name)
    storage_system = esxi_host.configManager.storageSystem
    print(storage_system)
    host_file_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo
    print(host_file_vol_mount_info)
    for host_mount_info in host_file_vol_mount_info:
    # if host_mount_info.volume.type == "VMFS": //List only type of datastores
        print(host_mount_info.volume.name)

