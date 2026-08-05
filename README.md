# GitHub & Git Cheatsheet

> A new Git/GitHub tip added every day for 365 days.
> Practical commands for React Native, Node.js, and web developers.

![Days](https://img.shields.io/badge/tips-86%20%2F%20365-blue)

## Tips So Far

<!-- TIPS_START -->
### Day 86 — List releases
`GitHub CLI` · 2026-08-05

```bash
gh release list
```

> See all published releases.

---
### Day 85 — Create a release
`GitHub CLI` · 2026-08-04

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "First release"
```

> Publish a new GitHub release.

---
### Day 84 — Assign issue to yourself
`GitHub CLI` · 2026-08-03

```bash
gh issue edit 42 --assignee @me
```

> Assign an issue to yourself quickly.

---
### Day 83 — Close an issue
`GitHub CLI` · 2026-08-02

```bash
gh issue close 42
```

> Close an issue from the terminal.

---
### Day 82 — View an issue
`GitHub CLI` · 2026-08-01

```bash
gh issue view 42
```

> Read a specific issue by number.

---
### Day 81 — List issues
`GitHub CLI` · 2026-07-31

```bash
gh issue list
```

> See all open issues in current repo.

---
### Day 80 — Create an issue
`GitHub CLI` · 2026-07-30

```bash
gh issue create --title "Bug: crash on login"
```

> Open a new GitHub issue from terminal.

---
### Day 79 — Close a PR
`GitHub CLI` · 2026-07-29

```bash
gh pr close 123
```

> Close a pull request without merging.

---
### Day 78 — Merge a PR
`GitHub CLI` · 2026-07-28

```bash
gh pr merge 123 --squash
```

> Merge a pull request using squash strategy.

---
### Day 77 — Checkout a PR
`GitHub CLI` · 2026-07-27

```bash
gh pr checkout 123
```

> Switch to the branch of a pull request locally.

---
### Day 76 — View a PR
`GitHub CLI` · 2026-07-26

```bash
gh pr view 123
```

> Read the details of a specific pull request.

---
### Day 75 — List open PRs
`GitHub CLI` · 2026-07-25

```bash
gh pr list
```

> See all open pull requests in current repo.

---
### Day 74 — Create a PR
`GitHub CLI` · 2026-07-24

```bash
gh pr create --title "feat: new feature" --fill
```

> Open a pull request from current branch.

---
### Day 73 — Fork a repo
`GitHub CLI` · 2026-07-23

```bash
gh repo fork owner/repo
```

> Fork a repository to your account.

---
### Day 72 — View repo in browser
`GitHub CLI` · 2026-07-22

```bash
gh repo view --web
```

> Open current repo in your default browser.

---
### Day 71 — List your repos
`GitHub CLI` · 2026-07-21

```bash
gh repo list
```

> See all your GitHub repositories.

---
### Day 70 — Clone a repo
`GitHub CLI` · 2026-07-20

```bash
gh repo clone owner/repo
```

> Clone any GitHub repository easily.

---
### Day 69 — Create a repo
`GitHub CLI` · 2026-07-19

```bash
gh repo create my-app --public
```

> Create a new GitHub repository from terminal.

---
### Day 68 — Check login status
`GitHub CLI` · 2026-07-18

```bash
gh auth status
```

> Verify you are logged in and see your username.

---
### Day 67 — Login to GitHub
`GitHub CLI` · 2026-07-17

```bash
gh auth login
```

> Authenticate with your GitHub account.

---
### Day 66 — Install GitHub CLI
`GitHub CLI` · 2026-07-16

```bash
brew install gh
```

> Install the official GitHub CLI on macOS.

---
### Day 65 — Delete a tag
`Tags` · 2026-07-15

```bash
git tag -d v1.0.0
```

> Remove a local tag.

---
### Day 64 — Push tags to remote
`Tags` · 2026-07-14

```bash
git push origin --tags
```

> Upload all local tags to remote.

---
### Day 63 — List all tags
`Tags` · 2026-07-13

```bash
git tag
```

> Show all tags in the repository.

---
### Day 62 — Create annotated tag
`Tags` · 2026-07-12

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
```

> Tag with a message — best practice for releases.

---
### Day 61 — Create a tag
`Tags` · 2026-07-11

```bash
git tag v1.0.0
```

> Mark a specific commit as a release version.

---
### Day 60 — Pull with rebase
`Remote` · 2026-07-10

```bash
git pull --rebase
```

> Pull and rebase instead of merge for cleaner history.

---
### Day 59 — Fetch without merging
`Remote` · 2026-07-09

```bash
git fetch origin
```

> Download remote changes without applying them.

---
### Day 58 — Change remote URL
`Remote` · 2026-07-08

```bash
git remote set-url origin https://github.com/user/new-repo.git
```

> Update the URL of an existing remote.

---
### Day 57 — Add a remote
`Remote` · 2026-07-07

```bash
git remote add origin https://github.com/user/repo.git
```

> Connect your local repo to a remote.

---
### Day 56 — View remote URLs
`Remote` · 2026-07-06

```bash
git remote -v
```

> See the fetch and push URLs for your remotes.

---
### Day 55 — Remove untracked files
`Undo` · 2026-07-05

```bash
git clean -fd
```

> Delete untracked files and directories.

---
### Day 54 — Discard all local changes
`Undo` · 2026-07-04

```bash
git checkout .
```

> Revert all unstaged changes in working directory.

---
### Day 53 — Add forgotten file to last commit
`Undo` · 2026-07-03

```bash
git add forgotten.js && git commit --amend --no-edit
```

> Add a file to the previous commit without changing message.

---
### Day 52 — Fix last commit message
`Undo` · 2026-07-02

```bash
git commit --amend -m "correct message"
```

> Change the message of your last commit before pushing.

---
### Day 51 — Revert a commit
`Undo` · 2026-07-01

```bash
git revert abc1234
```

> Create a new commit that undoes a specific commit safely.

---
### Day 50 — Undo and discard changes
`Undo` · 2026-06-30

```bash
git reset --hard HEAD~1
```

> Completely remove last commit and all changes. Dangerous!

---
### Day 49 — Undo last commit (unstage)
`Undo` · 2026-06-29

```bash
git reset HEAD~1
```

> Uncommit and unstage changes but keep files.

---
### Day 48 — Undo last commit (keep changes)
`Undo` · 2026-06-28

```bash
git reset --soft HEAD~1
```

> Uncommit but keep all your changes staged.

---
### Day 47 — Clear all stashes
`Stash` · 2026-06-27

```bash
git stash clear
```

> Delete all stashed entries at once.

---
### Day 46 — Drop a stash
`Stash` · 2026-06-26

```bash
git stash drop stash@{0}
```

> Delete a specific stash entry.

---
### Day 45 — Apply without removing
`Stash` · 2026-06-25

```bash
git stash apply
```

> Apply stash but keep it in the stash list.

---
### Day 44 — Apply latest stash
`Stash` · 2026-06-24

```bash
git stash pop
```

> Restore the latest stash and remove it from list.

---
### Day 43 — List stashes
`Stash` · 2026-06-23

```bash
git stash list
```

> See all saved stashes.

---
### Day 42 — Stash with a name
`Stash` · 2026-06-22

```bash
git stash push -m "wip: auth screen"
```

> Save stash with a descriptive label.

---
### Day 41 — Stash your work
`Stash` · 2026-06-21

```bash
git stash
```

> Temporarily save changes without committing.

---
### Day 40 — Squash commits
`Rebase` · 2026-06-20

```bash
git rebase -i HEAD~3 # change pick to squash
```

> Combine multiple commits into one clean commit.

---
### Day 39 — Interactive rebase
`Rebase` · 2026-06-19

```bash
git rebase -i HEAD~3
```

> Edit, squash, or reorder the last 3 commits.

---
### Day 38 — Continue after conflict
`Rebase` · 2026-06-18

```bash
git rebase --continue
```

> After fixing a conflict during rebase, continue the process.

---
### Day 37 — Abort a rebase
`Rebase` · 2026-06-17

```bash
git rebase --abort
```

> Cancel a rebase in progress and restore original state.

---
### Day 36 — Rebase onto main
`Rebase` · 2026-06-16

```bash
git rebase main
```

> Replay your branch commits on top of main.

---
### Day 35 — Mark conflict resolved
`Merging` · 2026-06-15

```bash
git add filename.js && git commit
```

> After fixing conflicts, stage and commit to complete merge.

---
### Day 34 — Check merge conflicts
`Merging` · 2026-06-14

```bash
git status
```

> After a conflict, git status shows which files need fixing.

---
### Day 33 — Abort a merge
`Merging` · 2026-06-13

```bash
git merge --abort
```

> Cancel an in-progress merge and go back to before.

---
### Day 32 — Merge with no fast-forward
`Merging` · 2026-06-12

```bash
git merge --no-ff feature/login
```

> Always create a merge commit for cleaner history.

---
### Day 31 — Merge a branch
`Merging` · 2026-06-11

```bash
git merge feature/login
```

> Merge another branch into your current branch.

---
### Day 30 — Push new branch to remote
`Branches` · 2026-06-10

```bash
git push -u origin feature/login
```

> Push and set upstream tracking for a new branch.

---
### Day 29 — Rename current branch
`Branches` · 2026-06-09

```bash
git branch -m new-name
```

> Rename the branch you are currently on.

---
### Day 28 — Delete remote branch
`Branches` · 2026-06-08

```bash
git push origin --delete feature/login
```

> Remove a branch from the remote repository.

---
### Day 27 — Force delete branch
`Branches` · 2026-06-07

```bash
git branch -D feature/login
```

> Delete a branch even if it has unmerged changes.

---
### Day 26 — Delete local branch
`Branches` · 2026-06-06

```bash
git branch -d feature/login
```

> Delete a branch that has been merged.

---
### Day 25 — List all branches
`Branches` · 2026-06-05

```bash
git branch -a
```

> Show local and remote branches.

---
### Day 24 — Modern create and switch
`Branches` · 2026-06-04

```bash
git switch -c feature/login
```

> Newer syntax to create and switch branches.

---
### Day 23 — Create and switch
`Branches` · 2026-06-03

```bash
git checkout -b feature/login
```

> Create a new branch and switch to it immediately.

---
### Day 22 — Switch to a branch
`Branches` · 2026-06-02

```bash
git checkout feature/login
```

> Switch your working directory to another branch.

---
### Day 21 — Create a branch
`Branches` · 2026-06-01

```bash
git branch feature/login
```

> Create a new branch without switching to it.

---
### Day 20 — Discard local changes
`Git Basics` · 2026-05-31

```bash
git restore filename.js
```

> Revert a file back to last committed state.

---
### Day 19 — Unstage a file
`Git Basics` · 2026-05-30

```bash
git restore --staged filename.js
```

> Remove a file from staging without losing changes.

---
### Day 18 — See staged changes
`Git Basics` · 2026-05-29

```bash
git diff --staged
```

> Show changes that are staged and ready to commit.

---
### Day 17 — See what changed
`Git Basics` · 2026-05-28

```bash
git diff
```

> Show unstaged changes in your working directory.

---
### Day 16 — See last 5 commits
`Git Basics` · 2026-05-25

```bash
git log --oneline -5
```

> Limit log output to the last 5 commits.

---
### Day 15 — Pretty log with graph
`Git Basics` · 2026-05-24

```bash
git log --oneline --graph --all
```

> Visualize branches and merges in the terminal.

---
### Day 14 — View commit history
`Git Basics` · 2026-05-23

```bash
git log --oneline
```

> See all commits in a compact one-line format.

---
### Day 13 — Pull latest changes
`Git Basics` · 2026-05-22

```bash
git pull
```

> Fetch and merge changes from the remote branch.

---
### Day 12 — Push to remote
`Git Basics` · 2026-05-21

```bash
git push origin main
```

> Upload your commits to the remote repository.

---
### Day 11 — Add and commit together
`Git Basics` · 2026-05-20

```bash
git commit -am "fix: typo in header"
```

> Stage tracked files and commit in one command.

---
### Day 10 — Commit with message
`Git Basics` · 2026-05-19

```bash
git commit -m "feat: add login screen"
```

> Save staged changes with a descriptive message.

---
### Day 9 — Stage one file
`Git Basics` · 2026-05-18

```bash
git add filename.js
```

> Stage a specific file only.

---
### Day 8 — Stage all changes
`Git Basics` · 2026-05-17

```bash
git add .
```

> Stage every changed file in current directory.

---
### Day 7 — Short status
`Git Basics` · 2026-05-16

```bash
git status -s
```

> Compact version of git status — M = modified, ? = untracked.

---
### Day 6 — Check status
`Git Basics` · 2026-05-15

```bash
git status
```

> See which files are staged, unstaged, or untracked.

---
### Day 5 — Clone a repo
`Git Basics` · 2026-05-14

```bash
git clone https://github.com/user/repo.git
```

> Download a remote repository to your machine.

---
### Day 4 — Initialize a repo
`Git Basics` · 2026-05-13

```bash
git init
```

> Start tracking a project with Git.

---
### Day 3 — Set your email
`Git Basics` · 2026-05-12

```bash
git config --global user.email "you@example.com"
```

> Set your email for all commits globally.

---
### Day 2 — Set your username
`Git Basics` · 2026-05-11

```bash
git config --global user.name "Your Name"
```

> Set your name for all commits globally.

---
### Day 1 — Check Git version
`Git Basics` · 2026-05-10

```bash
git --version
```

> Always know what version of Git you are running.

---
<!-- TIPS_END -->

---

*New tip added every day. Star the repo to follow along!*
