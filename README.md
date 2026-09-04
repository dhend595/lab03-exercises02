# Lab 03: Git and GitHub
This repository documents my practice with 
local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization
```text
total 0
drwxr-xr-x@ 3 douglashenderson  staff   96 Sep  4 14:35 .
drwxr-xr-x@ 8 douglashenderson  staff  256 Sep  4 14:35 ..
drwxr-xr-x@ 9 douglashenderson  staff  288 Sep  4 14:35 .git
```

### 1.2 First git status
```text
I accidently did a clear command out of habit here but I'm sure it was something about being on main and nothing to update if it was before I created the README or it was something like one untracked file if it was after I made the README
```

### 1.3 After the first commit
```text
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)

	new file:   README.md
```
### 1.4 git log
```text
6efc3b7 (HEAD -> main) Create lab README
```

### 1.5 git diff
```text
 
 ### 1.3 After the first commit
+```text
+On branch main
+Changes to be committed:
+  (use "git restore --staged <file>..." to unstage)
 
+       new file:   README.md
+```
 ### 1.4 git log
+```text
+6efc3b7 (HEAD -> main) Create lab README
+```
 
 ### 1.5 git diff
 
(END)
```

Paste the `git status` and `git diff` commands and their output.

How does this `git status` differ from the one in **1.2**?

### 1.6 Git command reflections

In one or two sentences each, what does each command do?

- `git init`: initializes a new Git repository in the current directory.
- `git status`: shows the current status of the working directory and staging area.
- `git add`: stages changes to be committed.
- `git commit`: records the staged changes in the repository.
- `git log`: shows the commit history.
- `git diff`: shows the differences between the working directory and the staging area.

### 1.7 Repository link

### 1.8 Comparing approaches

In your own words:

- How does the nested-loop approach check for a duplicate?
- How does the set-based approach check for a duplicate?
- What is the runtime and memory trade-off of each?

### 1.9 Pull request merge options

In your own words, what does each GitHub merge option do?

- Create a merge commit
- Squash and merge
- Rebase and merge