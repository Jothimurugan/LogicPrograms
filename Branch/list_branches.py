from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
repo = g.get_repo("Jothimurugan/LogicPrograms")
branches = repo.get_branches()
for branch in branches:
    print(branch.name)
    commited_files = branch.commit.files
    for filename in commited_files:
        print(filename.filename)
    