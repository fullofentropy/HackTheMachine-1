## Setting up project

### 1. Copy project into local directory
Navigate to the directory where you want to copy your project folder to, then enter command:

`git config --global credential.helper store
 git clone <project HTTP url>`


Then enter your username if prompted followed by your password (personal access token).

### 2. Configure git global variables
`git config --global user.name "<Your Name>"`<br>
`git config --global user.email "<youremail.navy.mil>"`


## Basic Git flow
1. `git checkout -b <branch>` Make a new branch whenever you want to add a new feature.
2. `git add file1 file2 ...` Make a changes to the code and stage them for commit.
3. `git commit -m <commit message>` Commit the changes when they are finalized.
4. Repeat steps 2 and 3 as needed until feature is working and complete.
5. `git pull origin main` Merge new feature branch with remote master branch in case any updates have been made to remote repository.
    a. Fix any merge conflicts and commit.
8. `git push` Update remote repository.
9. In GitHub, create pull request and merge with main branch.
10. (optional) `git branch -d <branch>` Delete branch now that it has been merged with master.


## Useful Commands

`alias graph='git log --all --decorate --oneline --graph'`: creates an alias so that you can see a graph of the project commits by using the command `graph`.

`git status`: see any changes to files since the last commit as well as any files that have been stages to commit.

`git add <file1> <file2> ...`: specify any files you want to be added to the next commit. Also referred to as staging the files.

`git commit -m <message>`: commit staged files and use \<message\> as the description for this commit.

`git commit -am <message>`: shortcut that allows you to stage and commit any files that have been previously committed and have changed.

`git fetch`: update origin/master to be updated with remote repository (i.e. Spork). Note that origin/master is not the same as the local master branch.

`git merge <branch name>`: merge branch \<branch name\> with current branch.

`git pull`: combines commands "git fetch origin/master" and "git merge origin/master" into one command to get and merge any changes in the remote repository (i.e. Spork) to the local branch.

`git push <remote repo> <branch in remote repo>`: publish local commits to branch in remote repository

`git checkout -b <branch name>`: create and checkout new branch with name \<branch name\>

`git checkout <branch name>`: switch to branch \<branch name\>. If the branch doesn't exist locally, but exists in a remote repository, it will copy over the one from the repository. Must be in a "clean working tree", so no changes must have been made since the last commit, can check with "git status".

`git branch`: see all local branches

`git branch -d <branch name>`: delete branch \<branch name\>. Must be in a different branch to do this.

`git branch -df <branch name>`: forcefully delete branch \<branch name\>. Careful, you cannot recover anything that hasn't been merged into other branches.

`git push origin --delete <branch name>`: delete remote branch \<branch name\>. This does not delete any local copies of the branch.
