from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")
repo = g.get_repo("Jothimurugan/LogicPrograms")
print(repo)

#, tree, parents, author=NotSet, committer=NotSet
message = "Trying Auto commit"
repo.create_file("Jothimurugan/LogicPrograms/", message, "Jothimurugan/LogicPrograms/", branch="GitHubAutomation", committer=NotSet, author=NotSet)
repo.create_git_commit(message, tree, parents, author=NotSet, committer=NotSet)