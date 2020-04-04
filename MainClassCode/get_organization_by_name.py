#Need to check code

from github import Github

g = Github("Jothimurugan", "Qbpp6sG9")

org = g.get_organization("Jothimurugan")
org.login