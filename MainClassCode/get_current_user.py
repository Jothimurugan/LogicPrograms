from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
user = g.get_user()
print(user.login)

