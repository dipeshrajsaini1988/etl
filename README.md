# etl
personal etlprojects 
git init
git add <filename.extention>
git commit -m  "your comments"
git push origin main

git switch -c <new branch name>
# make changes to the files
git add . 
git commit -m "Implement new feature"
git push --set-upstream origin <new branch name>

# to check your branch
git branch

# to merge
# Switch to the main branch
git switch main
# Pull the latest changes from GitHub to prevent conflicts
git pull origin main
# Merge the feature branch into your current branch (main)
git merge new-feature-branch
# push merged changes
git push origin main

# delete branch locally
git branch -d <branch name>

# delete branch on remote
git push origin --delete <branch name>

# to fetch all from origin
git fetch origin

-- test line



git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"


dipeshrajsaini1988
drsaini123!!
dipesh.saini@gmail.com
