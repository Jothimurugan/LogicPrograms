from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
repo = g.get_repo("Jothimurugan/LogicPrograms")
l = repo.get_branches()
for branch in l:
    print(branch.name)
