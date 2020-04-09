from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj

for x in range(1,14):
    if (x == 5):
        continue
    vm = get_obj(contents, [vim.VirtualMachine],"Clone_VM_00"+str(x))
    destination_ds = get_obj(contents, [vim.HostSystem], "datera_iscsib07b95e741614023a7a4e8427146ea36-1586339288.80095")
    destination_host = get_obj(contents, [vim.HostSystem], "172.19.3.252")
    resource_pool = vm.resourcePool
    migrate_priority = vim.VirtualMachine.MovePriority.defaultPriority

# task = vm.Migrate(pool=resource_pool, host=destination_host, priority=migrate_priority)
    relocate_spec = vim.vm.RelocateSpec(datastore= destination_ds, host=destination_host)
    task = vm.Relocate(relocate_spec)
    print("svMotion is going on..")
