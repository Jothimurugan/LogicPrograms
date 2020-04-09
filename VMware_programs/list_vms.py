from pyVim import connect
import atexit
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.VirtualMachine], True)
print(obj_view)
VMs = obj_view.view
# print(Datacenters)
creds = vim.vm.guest.NamePasswordAuthentication(username="root", password="rts")
pm = contents.guestOperationsManager.processManager

ps = vim.vm.guest.ProcessManager.ProgramSpec(
                programPath="/usr/bin/fio",
                arguments="--name 4k_write_100MB --ioengine=libaio --bs=4m --group_reporting --rw=randrw --filename=/dev/sdb --size=100% --direct=1 --status-interval=10 --randrepeat=0"
            )

for vm in VMs:
    if vm.name == "Clone_VM_001":
        '''
        vm.MountToolsInstaller()
        vm.UpgradeTools_Task()
        '''
        res = pm.StartProgramInGuest(vm, creds, ps)
        print("process pid  {}".format(res))
        processes = pm.ListProcessesInGuest(vm,creds)
        print(processes)
    # print(type(vm))
    # print(vm.name)

atexit.register(connect.Disconnect, s_conn)