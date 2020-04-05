from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.ClusterComputeResource], True)
# print(obj_view)
Clusters = obj_view.view
# print(Clusters)


for cluster in Clusters:
    print(cluster.configuration)
    print(type(cluster))




