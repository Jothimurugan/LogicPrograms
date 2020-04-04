from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
repo_name = g.get_repo("")
print(repo_name.name)