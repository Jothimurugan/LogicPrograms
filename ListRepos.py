from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")

#List repositories
for repo in g.get_user().get_repos():
    # print(type(repo))
    print(repo) #print repo full detail
    print(repo.owner) # print repo owner
    print(repo.downloads_url)
    print(repo.id)
    # print(repo.master_branch)

#Listing repo in list data format using list comprehensio

# repo = [x for x in g.get_user().get_repos()]
# print(repo)