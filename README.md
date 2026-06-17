# GitHub & Git Cheatsheet

> A new Git/GitHub tip added every day for 365 days.
> Practical commands for React Native, Node.js, and web developers.

![Days](https://img.shields.io/badge/tips-37%20%2F%20365-blue)

## Tips So Far

<!-- TIPS_START -->
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
