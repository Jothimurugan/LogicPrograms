from pyVim import connect
from pyVmomi import vim

s_conn = connect.SmartConnectNoSSL(host="172.58.7.182", user="Administrator@vsphere.local", pwd="Cert123#")
contents = s_conn.RetrieveContent()

obj_view = contents.viewManager.CreateContainerView(contents.rootFolder, [vim.Datacenter], True)
print(obj_view)
f = obj_view.view

for datacenter in f:
    if datacenter.name == "Datacenter":
        obj_view1 = contents.viewManager.CreateContainerView(datacenter.hostFolder, [vim.ClusterComputeResource], True)
        Clusters = obj_view1.view
        # print(Clusters)
        for cluster in Clusters:
            print(cluster.name)
            hostspec = vim.host.ConnectSpec()
            hostspec.hostName = "172.58.4.71"
            hostspec.userName = "root"
            hostspec.password = "rts12345!"
            print(hostspec)
            asConnected = True
            cluster.AddHost_Task(hostspec, asConnected)

