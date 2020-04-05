from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.Datacenter], True)
print(obj_view)
f = obj_view.view
print(f)
for x in f:
    # print(x.name)
    if x.name == "newDC":
        # print(type(x))
        cluster_spec = vim.cluster.ConfigSpec()
        print(type(cluster_spec))
        # cluster_spec.drsConfig.enabled = True
        print(cluster_spec)
        x.hostFolder.CreateCluster(name="NewCluster1", spec=cluster_spec)