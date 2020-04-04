from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
username = g.get_user("Jothimurugan")
print(username.name)