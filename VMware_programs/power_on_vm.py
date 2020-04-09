from pyVim import connect
import atexit
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.VirtualMachine], True)
print(obj_view)
VMs = obj_view.view
# print(Datacenters)
for vm in VMs:
    if vm.name == "Clone_VM_001":
        print(vm.runtime.powerState)
        # if vm.runtime.powerState == "poweredOff":
        #     vm.PowerOnVM_Task()
        # vm.CloneVM_Task()
        print(contents.rootFolder.name)

atexit.register(connect.Disconnect, s_conn)