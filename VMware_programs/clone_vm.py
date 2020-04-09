from pyVim import connect
import atexit
from pyVmomi import vim

def _get_obj(content, vimtype, name):
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

def get_cluster(si, name):
    """
    Find a cluster by it's name and return it
    """
    return _get_obj(si.RetrieveContent(), [vim.ComputeResource], name)

def get_vm_by_name(si, name):
    """
    Find a virtual machine by it's name and return it
    """
    return _get_obj(si.RetrieveContent(), [vim.VirtualMachine], name)

s_conn = connect.SmartConnectNoSSL(host="172.19.3.110", user="Administrator@vsphere.local", pwd="Cert123#")
# contents = s_conn.RetrieveContent()
contents = s_conn
template_vm = get_vm_by_name(contents, "Clone_VM_001")
cluster = get_cluster(contents, "NewCluster")
relocate_spec = vim.vm.RelocateSpec(pool=cluster.resourcePool)
# guest_customization_spec = contents.customizationSpecManager.GetCustomizationSpec(name=customization_spec_name)
# This constructs the clone specification and adds the customization spec and location spec to it
cloneSpec = vim.vm.CloneSpec(powerOn=True, template=False, location=relocate_spec)

# Finally this is the clone operation with the relevant specs attached
for x in range(6,14):
    clone = template_vm.Clone(name="Clone_VM_00"+str(x), folder=template_vm.parent, spec=cloneSpec)
    print("Clone is done for {}".format("Clone_VM_00"+str(x)))
print("Clone is done")

atexit.register(connect.Disconnect, s_conn)
