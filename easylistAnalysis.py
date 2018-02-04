import git
from git import Repo
COMMITS_TO_PRINT = 5

repo = Repo("/Users/paunov/Programming/easylist")
assert not repo.bare

fifty_first_commits = list(repo.iter_commits('master', max_count=50))
print repo.commit(fifty_first_commits)

# First create a Github instance:

# using username and password
#gh = git("alexpaunov", "penguinl2sh89")

#user = gh.get_user()
#easyRep = user.get_repo('easylist')




# Then play with your Github objects:
#for repo in gh.get_user().get_repos():
#   print(repo.name)


#for c in gh.commits.forBranch('alexpaunov', 'easylist'):
#   print("%s %s" % (c.id[:7], c.message[:60].split("\n")[0]))




