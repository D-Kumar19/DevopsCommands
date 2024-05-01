# Git Commands Guide 📘

Welcome to the Git Commands Guide! This document is designed to help you navigate and utilize various Git commands efficiently. Git is an indispensable tool for version control, allowing teams and individual developers to track changes, revert to previous stages, and collaborate on projects seamlessly. Whether you're a beginner looking to understand the basics or an experienced developer seeking a quick reference, this guide is here to assist.

## Help Commands 🆘

Getting help with Git commands is straightforward and can be incredibly useful when you're learning new features or need a quick reminder. Below you'll find detailed instructions on how to access help for different Git commands directly from your command line.

| Command                 | Description                                                                                                                                                                                |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git help <command>`    | Shows detailed help for the specified command. Examples include:                                                                                                                           |
|                         | - `git help config` - Displays help for configuring user-specific and repository-specific settings.                                                                                        |
|                         | - `git help init` - Provides details on creating a new Git repository.                                                                                                                     |
|                         | - `git help clean` - Explains how to remove untracked files from the working directory.                                                                                                    |
|                         | - `git help log` - Offers guidance on displaying commit logs.                                                                                                                              |
| `git <command> --help`  | This is another way to access help, equivalent to the `git help` form.                                                                                                                     |
|                         | Examples:                                                                                                                                                                                  |
|                         | - `git config --help` - Opens help for the configuration command.                                                                                                                          |
|                         | - `git init --help` - Shows help information for initializing new repositories.                                                                                                            |
|                         | - `git clean --help` - Provides help for the clean command, which deletes untracked files.                                                                                                 |
|                         | - `git log --help` - Displays help for viewing the commit history.                                                                                                                         |
| `git <command> -h`      | A shorthand for help, providing quick access to command summaries.                                                                                                                         |
|                         | Examples:                                                                                                                                                                                  |
|                         | - `git config -h` - Shows a summary of configuration command options.                                                                                                                      |
|                         | - `git init -h` - Displays a quick summary of the init command options.                                                                                                                    |
|                         | - `git clean -h` - Summarizes the clean command's usage and options.                                                                                                                       |
|                         | - `git log -h` - Provides a brief overview of log command options.                                                                                                                         |

## Basic Navigation Commands 🧭

Before diving deeper into Git, it's crucial to be comfortable with basic command line navigation. These commands help you move around the filesystem and manage files directly from the terminal, forming the foundation for using Git effectively.

| Command        | Description                                                                                                                                                                                         |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pwd`          | Prints the current working directory. This command lets you see where you currently are in the filesystem.                                                                                          |
| `ls`           | Lists all files and directories in the current directory. Use `ls -l` for a detailed listing.                                                                                                       |
| `cd <path>`    | Changes the current directory to `<path>`. For example, `cd Documents` changes the current directory to `Documents`.                                                                                |
| `mkdir <dir>`  | Creates a new directory named `<dir>`. For example, `mkdir new_folder` creates a new directory called `new_folder`.                                                                                 |
| `touch <file>` | Creates a new empty file named `<file>`. For example, `touch example.txt` creates an empty file named `example.txt`.                                                                                |
| `code <file>`  | Opens the specified `<file>` in Visual Studio Code. If the file does not exist, Visual Studio Code will create it. For example, `code README.md` opens or creates the README.md file.               |

## Global Flag Commands 🌐

Git's global settings configure user information, editor preferences, and more across all local repositories on your system. These commands allow you to set up your Git environment just the way you like it, making your interactions with Git smoother and more tailored to your workflow.

| Command                                                         | Description                                                                                                                                        |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| `git --version`                                                 | Displays the version of Git installed on your system.                                                                                              |
| `git config --global user.name "<name>"`                        | Sets the name that will be attached to your commits and tags globally across all repositories. Example: `git config --global user.name "John Doe"`.|
| `git config --global user.email "<email>"`                      | Sets the email address that will be attached to your commits and tags globally. Example: `git config --global user.email "johndoe@example.com"`.   |
| `git config --global core.editor "editor"`                      | Sets the default text editor for Git commands globally, such as for commit messages.                                                               |
|                                                                 | Examples:                                                                                                                                          |
|                                                                 | - `git config --global core.editor "nano"` - Sets Nano as the default editor for Git commands.                                                     |
|                                                                 | - `git config --global core.editor "vim"` - Sets Vim as the default editor for Git commands.                                                       |
|                                                                 | - `git config --global core.editor "emacs"` - Sets Emacs as the default editor for Git commands.                                                   |
|                                                                 | - `git config --global core.editor "code --wait"` - Sets Visual Studio Code as the default editor, waiting for files to close before returning.    |
|                                                                 | - `git config --global core.editor "subl -n -w"` - Sets Sublime Text as the default editor, with no windows reusing and wait mode.                 |
| `git config --global init.defaultBranch main`                   | Sets 'main' as the default branch name for all new repositories created on your system. It can be set as `master` or any other branch if in use.   |
| `git config --global alias.aliasname "<command>"`               | Creates a shortcut (alias) for a Git command.                                                                                                      |
|                                                                 | Examples:                                                                                                                                          |
|                                                                 | - `git config --global alias.s "status"` - Simplifies `git status` to `git s`.                                                                     |
|                                                                 | - `git config --global alias.co "checkout"` - Simplifies `git checkout` to `git co`.                                                               |
|                                                                 | - `git config --global alias.ci "commit"` - Simplifies `git commit` to `git ci`.                                                                   |
|                                                                 | - `git config --global alias.br "branch"` - Simplifies `git branch` to `git br`.                                                                   |
|                                                                 | - `git config --global alias.lg "log --graph --oneline --decorate --all"` - Enables a decorated graphical log view with `git lg`.                  |
| `git config --global auto.crlf true` or `input`                 | Configures Git to handle line endings in files for cross-platform projects. Use `true` for Windows or `input` for Unix-like systems.               |
| `git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"` | Sets up Visual Studio Code as the diff tool for viewing changes between commits.                                                     |
| `git difftool`                                                  | Opens the configured diff tool to compare changes in files. In our case, Visual Studio Code if set.                                                |
| `git config --global -e`                                        | Opens the global configuration file in the default editor for manual editing.                                                                      |
| `git config --list`                                             | Displays all the current Git configuration settings locally.                                                                                       |
| `git config --global --list`                                    | Displays all global Git configuration settings.                                                                                                    |
| `git config --list --show-origin`                               | Displays all Git configurations along with their origins, showing where each setting is defined.                                                   |

## Creating the First Commit 🚀

Starting with Git involves initializing a repository, staging changes, and making your first commit. These commands will guide you through setting up your project and taking the initial steps in version control management, marking the beginning of your project's history.

| Command                           | Description                                                                                                                                                                      |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git init`                        | Initializes a new Git repository in the current directory. This is the first step in setting up version control for your project.                                                |
| `git status`                      | Displays the state of the working directory and the staging area, showing which changes have been staged, which haven't, and which files aren't tracked.                         |
| `git status -s`                   | Shows the status in a short, condensed format, making it easier to quickly see changes.                                                                                          |
| `git add <file_name>`             | Adds a specific file to the staging area, preparing it for a commit. Example: `git add example.txt`.                                                                             |
| `git add --all`                   | Adds all new and changed files to the staging area. This includes all files in the entire repository.                                                                            |
| `git add -A`                      | Similar to `git add --all`, adds all changes from the entire working tree to the staging area.                                                                                   |
| `git add .`                       | Adds new and modified files in the current directory to the staging area. This does not add removed files.                                                                       |
| `git commit -m "message"`         | Records changes to the repository with a descriptive message. Example: `git commit -m "Initial commit"`.                                                                         |
| `git commit -a -m "message"`      | Combines adding changes and committing them in one step for modified and deleted files (but not new files). Example: `git commit -a -m "Updated configs"`.                       |
| `git commit --amend`              | Opens the default configured text editor for modifying the most recent commit.                                                                                                   |
| `git commit --amend -m "message"` | Modifies the most recent commit. This can be used to correct typos in the previous commit's message.                                                                             |
| `git commit --amend --no-edit`    | Modifies the most recent commit without changing its commit message.                                                                                                             |

## Undoing Changes and Comparing Differences 🔄

Managing changes effectively is a crucial aspect of version control with Git. This section provides detailed commands for undoing changes and comparing different states of your repository. Whether you need to revert changes, compare updates, or simply review historical modifications, the following commands will guide you through managing your project's evolution safely and efficiently.

### File Operations in Git 🗂️

Managing files efficiently within a Git repository is crucial for maintaining an organized and clean working environment. This section covers essential commands for renaming and deleting files, as well as removing untracked files to ensure your repository stays tidy.

#### Rename and Delete Files 🔀🗑️

Renaming or deleting files in Git can be done using simple commands that also stage these changes for commit, making these operations seamless and efficient.

| Command                                             | Description                                                                                                                                                    |
|:------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git mv <old_file> <new_file>`                      | Renames a file and stages the change. This is the simplest way to rename a file in Git.                                                                        |
| `git rm <file>`                                     | Deletes a file and stages the deletion. This is straightforward for removing files from tracking.                                                              |
| `git mv <old_file> <new_file> && git rm <old_file>` | Renames a file and then deletes the old one in two steps if needed for more control over the operations.                                                       |

#### Cleaning Untracked Files 🧹

Sometimes your working directory can get cluttered with build outputs, log files, or other untracked files. Git provides a powerful command to clean your working directory to revert it back to a clean state.

| Command                                             | Description                                                                                                                                                    |
|:------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git clean`     | Remove untracked files from the working directory. By default, it does not remove directories.                                                                                                     |
| `git clean -fd` | Removes all untracked files and directories. The `-f` is for force, and `-d` tells Git to remove directories as well.                                                                              |

### Undoing Changes 🔙

Sometimes you need to undo changes or clean up your working directory. Whether you accidentally staged files, committed wrong changes, or simply need to revert to a previous state, Git provides powerful tools to revert these actions without losing data.

| Command                                   | Description                                                                                                                                                              |
|:------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git rm <file_name>`                      | Removes a file from the working directory and stages the deletion. Example: `git rm example.txt`.                                                                        |
| `git rm .`                                | Removes all files from the current directory and stages the deletions.                                                                                                   |
| `git rm --cached <file_name>`             | Removes a file from the staging area but leaves it in the working directory. Example: `git rm --cached example.txt`.                                                     |
| `git rm --cached .`                       | Removes all files from the staging area but leaves them in the working directory.                                                                                        |

### Restoring Changes 🔄

Restoring files to a previous state can help in quickly fixing mistakes by pulling data from earlier commits or the staging area.

| `git restore <file_name>`                 | Restores a file from the staging area back to the working directory. Example: `git restore example.txt`.                                                                 |
| `git restore ./`                          | Restores all files in the current directory from the staging area back to the working directory.                                                                         |
| `git restore --staged <file_name>`        | Unstages a file while keeping the changes in the working directory. Example: `git restore --staged example.txt`.                                                         |
| `git restore --staged ./`                 | Unstages all changes in the current directory while keeping changes in the working directory.                                                                            |
| `git restore --source=HEAD~1 <file_name>` | Restores a file to a previous version from one commit ago. Example: `git restore --source=HEAD~1 example.txt`.                                                           |
| `git restore --staged --worktree <file>` or `./`               | Unstages changes to a file and restores the file to the state it has in the current commit, keeping the changes in the working directory.           |
| `git restore --source=HEAD --staged --worktree <file>` or `./` | Resets a file to the state it has in the latest commit (`HEAD`), both in the staging area and the working directory.                                |

### Comparing Changes 📊

Git offers a robust set of tools for comparing changes across commits, branches, or even different stages of the staging area. Understanding these differences is vital for effective team collaborations and individual work.

| Command                                   | Description                                                                                                                                                              |
|:------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git diff`                                | Shows changes between the working directory and the staging area.                                                                                                        |
| `git diff --staged`                       | Shows changes between the staging area and the last commit, also accessible via `--cached`.                                                                              |
| `git diff --cached`                       | Alias for `--staged`, showing changes between the staging area and the last commit.                                                                                      |
| `git diff HEAD`                           | Shows changes between the current working directory and the last commit (HEAD). This highlights what has been changed but not yet staged.                                |
| `git difftool --staged`                   | Opens a GUI tool to show differences between the staging area and the last commit.                                                                                       |
| `git diff <branch_name>`                  | Shows changes between the working directory and the named branch. Example: `git diff main`.                                                                              |
| `git diff <branch_name1>..<branch_name2>` | Shows changes between two branches. Example: `git diff main..feature`.                                                                                                   |
| `git diff <sha_value>`                    | Shows changes between the working directory and the commit identified by SHA. Example: `git diff 3a0b9ec`.                                                               |
| `git diff <sha_value1>..<sha_value2>`     | Shows changes between two specific commits. Example: `git diff 3a0b9ec..97d1e98`.                                                                                        |

## Viewing Commit History 📜

The ability to view and understand the commit history is what makes Git such a powerful tool for version control. Each command listed in this section helps you visualize the history of your project in different formats, from detailed commit information to a high-level overview. These insights can be critical for debugging issues, understanding project evolution, and making informed decisions about future development.

| Command                                      | Description                                                                                                                                                           |
|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git show <sha_value>`                       | Displays detailed information about a specific commit or object identified by its SHA hash.                                                                           |
| `git show HEAD~1:<file_name>`                | Shows the contents of a specific file as it was in the commit one before the current HEAD.                                                                            |
| `git log`                                    | Displays the full commit history of the current branch, listing each commit with its SHA, author, date, and message.                                                  |
| `git log -p`                                 | Shows the patch representing each commit, displaying the exact changes made in each commit alongside the commit details.                                              |
| `git log --oneline`                          | Condenses each commit to a single line, showing a short SHA and the commit message.                                                                                   |
| `git log --oneline --reverse`                | Displays all commits in reverse order, starting from the oldest to the most recent, in a condensed one-line format.                                                   |
| `git log --oneline --graph --decorate --all` | Shows a visual graph of all branches, tags, and commits, decorated and condensed into one-line entries.                                                               |
| `git log --author='<name>'`                  | Shows commits authored by `<name>`. For example, `git log --author='John'` will only show commit made by `John`.                                                      |
| `git log --grep='<something>'`               | Searches commit messages for the term `something`. For example, `git log --grep='bug fix'` will only show commit that include `bug fix` in description.               |

## Exploring Git Repository Objects 🔍

Dive deeper into the structure of your Git repository with these commands, which allow you to list tracked files, explore tree objects, and examine the details of specific commits or blobs. Understanding these elements will enable you to manage and diagnose your repository’s content more effectively.

| Command                       | Description                                                                                                                                                                          |
|:------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git ls-files`                | Lists all the files currently being tracked by Git in the repository. This command helps you see which files are included in the version control system.                             |
| `git ls-tree <commit>`        | Lists the contents of a tree object corresponding to a commit. This shows directories and files in a commit, helping to visualize the structure at that point in history.            |
| `git cat-file -t <sha_value>` | Displays the type of the object stored in Git's database with the specified SHA. Example: `git cat-file -t 3a0b9ec` might output `commit`, `blob`, or `tree`, depending on the type. |
| `git cat-file -p <sha_value>` | Prints the content of the object specified by its SHA. Example: `git cat-file -p 3a0b9ec` could show the contents of a commit, a file (blob), or a directory structure (tree).       |

## GitIgnore File 🚫

The .gitignore file is a text file that tells Git which files or directories to ignore in a project. A typical .gitignore file will contain patterns that match file names or directories, and it can include standard glob patterns which allow for flexible matching. For example:

1. Ignore all .log files: *.log
2. Ignore a specific directory: node_modules/

## Resetting Changes 🔄

Whether you need to undo changes or completely revert your repository to a previous state, the git reset command offers powerful options. From soft resets that preserve changes in your working directory to hard resets that clean your working tree, mastering these commands is crucial for correcting mistakes and maintaining a clean project history.

| Command                            | Description                                                                                                                                                                     |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git reset`                        | Resets the staging area to match the latest commit but does not affect the working directory or current branch, effectively unstaging all staged changes.                       |
| `git reset --hard`                 | Resets the staging area and the working directory to match the current HEAD. This command discards all changes in both the staging area and the working directory.              |
| `git reset --soft`                 | Resets only the HEAD to the current commit without touching the staging area or the working directory.                                                                          |
| `git reset --mixed`                | Resets the staging area to match the HEAD but does not affect the working directory. This is the default mode for git reset.                                                    |
| `git reset --keep`                 | Resets the current HEAD to the specified commit, but unlike `--hard`, it keeps your local changes as long as they do not conflict with the files that are reset.                |
| `git reset <sha_value>`            | Moves the current branch's tip backward to the specified commit (`<sha_value>`), unstaging changes that occurred after that commit but keeping them in the working directory. Here we can add flags as well. Such as `--soft` to move the HEAD but not touch staging and working directory. `--mixed` to unstage the changes and moving them to working tree. `--hard` to move the HEAD and discard all changes. `--keep` to move the HEAD but keep the changes.                                                                                                                                                           |
| `git reset HEAD~<number>`          | Resets the repository to `<number>` commits before the current HEAD. This number can be any positive integer. The same way we can use `--soft` to move the HEAD but not touch staging and working directory. `--mixed` to unstage the changes and moving them to working directory. `--hard` to move the HEAD and discard all changes. `--keep` to move the HEAD but keep the changes.               |

## Branching, Merging, and Rebasing Commands 🌿

Effective branch management is key to a well-maintained Git repository. This section covers everything from creating and deleting branches to sophisticated techniques like merging and rebasing. These commands not only help manage features and fixes but also facilitate smooth collaboration among multiple contributors.

### Branching 🌱

Branching is fundamental in Git to enable simultaneous work on multiple features within the same repository. Learn how to list, create, rename, and delete branches to manage your development effectively.

| Command                                    | Description                                                                                                                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git branch`                               | Lists all existing branches in the repository.                                                                                                                          |
| `git branch -a`                            | Lists all branches, including remote-tracking branches.                                                                                                                 |
| `git branch -r`                            | Lists remote-tracking branches only.                                                                                                                                    |
| `git branch --list`                        | Lists both local and remote-tracking branches.                                                                                                                          |
| `git branch --merged`                      | Lists the branches that have been merged into the current branch.                                                                                                       |
| `git branch <branch_name>`                 | Creates a new branch with the specified name. Example: `git branch new_feature`.                                                                                        |
| `git branch -m <new_branch_name>`          | Renames the current branch to the specified name. Example: `git branch -m new_feature_v2`.                                                                              |
| `git branch -d <branch_name>`              | Deletes the specified branch. Example: `git branch -d old_branch`.                                                                                                      |
| `git checkout <branch_name>`               | Switches to the specified branch. Example: `git checkout development`.                                                                                                  |
| `git checkout -b <new_branch_name>`        | Creates a new branch with the specified name and switches to it. Example: `git checkout -b feature_x`.                                                                  |
| `git switch <branch_name>`                 | Switches to the specified branch. Example: `git switch hotfix`.                                                                                                         |
| `git switch -c <new_branch_name>`          | Creates a new branch with the specified name and switches to it. Example: `git switch -c experimental_feature`.                                                         |

### Merging 🤝

Merging is a critical process for integrating changes from one branch into another. This subsection provides commands for merging branches, including how to handle fast-forward merges and create merge commits to preserve history.

| Command                                    | Description                                                                                                                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git merge <branch_name>`                  | Merges the specified branch into the current branch. Example: `git merge feature_branch`.                                                                               |
| `git merge -m "message" <branch_name>`     | Merges the specified branch into the current branch with a custom commit message. Example: `git merge -m "Merge feature_x" feature_x`.                                  |
| `git merge <branch_name> --no-ff`          | Merges the specified branch into the current branch, creating a merge commit even if it's a fast-forward merge. Example: `git merge feature_branch --no-ff`.            |

### Rebasing 🧵

Rebasing is an alternative to merging, offering a way to move or "rebase" a series of commits onto a new base. It’s useful for cleaning up your commit history before merging changes into another branch. Learn how to perform rebasing safely and resolve conflicts when they occur.

| Command                                    | Description                                                                                                                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git rebase <branch_name>`                 | Rebases the current branch onto the specified branch. Example: `git rebase master`.                                                                                     |
| `git rebase --continue`                    | Continues the rebase operation after resolving conflicts.                                                                                                               |
| `git rebase --skip`                        | Skips the current patch during a rebase operation.                                                                                                                      |
| `git rebase --abort`                       | Aborts the current rebase operation and restores the branch to its state before the rebase started.                                                                     |

## Tag Commands 🏷️

Tags in Git serve as important milestones and reference points within your project's history. They are typically used to mark release points (e.g., v1.0, v2.0) because they create permanent historical references to a specific state of the repository. This section covers everything you need to know about creating, viewing, and managing tags in Git, whether they are lightweight or annotated.

| Command                                                   | Description                                                                                                                                              |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git tag --list`                                          | Lists all tags in the repository.                                                                                                                        |
| `git show <tag>`                                          | Displays information about the specified tag, including the commit it points to and its associated metadata.                                             |
| `git tag <tag>`                                           | Creates a lightweight tag at the current commit. Example: `git tag v1.0.0`.                                                                              |
| `git tag <tag> <previous_commit>`                         | Creates a lightweight tag at the specified commit. Example: `git tag v1.0.0 HEAD~2`.                                                                     |
| `git tag -a <annotated_tag> <commit_hash> -m "message"`   | Creates an annotated tag at the specified commit with a custom message. Example: `git tag -a v1.0.0 HEAD -m "Release 1.0.0"`.                            |
| `git cat-file -t <tag>`                                   | Displays the type of object pointed to by the lightweight tag.                                                                                           |
| `git cat-file -p <tag>`                                   | Displays the content (commit hash) pointed to by the lightweight tag.                                                                                    |
| `git cat-file -t <annotated_tag>`                         | Displays the type of object pointed to by the annotated tag.                                                                                             |
| `git cat-file -p <annotated_tag>`                         | Displays the content (commit hash) and message of the annotated tag.                                                                                     |
| `git tag -d <tag>`                                        | Deletes a local tag. Example: `git tag -d v1.0.0`.                                                                                                       |
| `git push --delete origin <tag>`                          | Deletes a tag on the remote repository. Example: `git push --delete origin v1.0.0`.                                                                      |
| `git push --tag`                                          | Pushes tags to the remote repository.                                                                                                                    |

## Syncing Changes with Remote Repositories in Git 🔄

In this section, you'll find the essential commands to set up and manage remote repositories. Whether you're working with a central repository on a platform like GitHub or maintaining a connection to a fork's original source, these commands help you establish and visualize remote links necessary for collaborative development.

### Clone Repository 🌐

| Command                     | Description                                                                                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git clone <repo_link>`     | Clone a repository into a directory named after the repo.                                                                                                                              |
| `git clone <repo1> <repo2>` | Clone from `repo1` into `repo2`, a specific directory.                                                                                                                                 |

### Add Origin ➕

Adding an 'origin' is crucial for defining the primary remote source of your repository. This typically points to the repository from which you directly push and pull changes. Additionally, setting up an 'upstream' is fundamental for working with forks, allowing you to stay updated with the original repository.

| Command                               | Description                                                                                                                                                                  |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git remote add origin <origin_link>` | Add 'origin' as a remote. This is typically the primary repository on services like GitHub, GitLab, or Bitbucket.                                                            |
| `git remote add upstream <repo_link>` | Add 'upstream' as a remote. Useful for forks to keep track of the original repository.                                                                                       |
| `git remote -v`                       | List all configured remotes to check URLs associated with `origin` and `upstream`.                                                                                           |
| `git remote show origin`              | Show detailed information about the 'origin' remote, including fetch and push URLs.                                                                                          |
| `git branch -M main`                  | Rename the default branch locally to 'main'.                                                                                                                                 |

### Pull and Push 📤📥

This subsection explains how to sync your changes with remote repositories. Pushing commits to your remote branches and pulling updates from them are everyday activities in a developer’s workflow. Master these commands to ensure your repository remains in sync with others’ work and to prevent conflicts.

| Command                                        | Description                                                                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `git push -u origin main`                      | Push the 'main' branch to 'origin' and set it to track the remote branch.                                                                                           |
| `git push --set-upstream origin <branch_name>` | Push a new branch to 'origin' and set it to track the remote branch. This is only needed the first time.                                                            |
| `git push --all`                               | Push all local branches to their corresponding remote branches.                                                                                                     |
| `git pull --all`                               | Fetch and pull changes from all tracked branches from the remote repository.                                                                                        |
| `git fetch`                                    | Fetch updates from the remote repository without merging them into the local branch.                                                                                |
| `git merge`                                    | Merge changes from the fetched remote branch into the current local branch.                                                                                         |
| `git pull`                                     | Fetch and merge changes from the remote branch to the local branch in one command.                                                                                  |
| `git fetch upstream`                           | Fetch changes from the 'upstream' remote repository, typically used to keep a fork up to date.                                                                      |
| `git merge upstream/<branch>`                  | Merge changes from a specific branch of 'upstream' into the current branch.                                                                                         |
| `git pull upstream <branch>`                   | Pull changes directly from an 'upstream' branch, combining fetch and merge in one step.                                                                             |




ssh-keygen -t rsa -b 4096 -C "email address"
name of the gile and passphrase put and later cat it out maybe
add public key to github and try to push something (just for checking purpoese)

## Cloning a Repository Using SSH 🗝️

Using SSH to clone repositories provides a secure way to authenticate to GitHub without entering your username and password each time you interact with the repository. Follow these simple steps to set up SSH for GitHub and clone a repository.

### 1. Generate SSH Key

- **Open Terminal:** Start by opening your terminal.
- **Generate Key:** Run the command:

  ```bash
  ssh-keygen -t ed25519 -b 4096 -C "your_email@example.com"
  ```

  Replace `"your_email@example.com"` with your GitHub email. Press Enter to accept the default file location and passphrase.

### 2. Add SSH Key to SSH Agent

- **Start the SSH Agent:**

  ```bash
  eval "$(ssh-agent -s)"
  ```

- **Add SSH Key:**

  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```

### 3. Add Public Key to GitHub

- **Copy SSH Public Key:**

  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```

  Copy the output.

- **Add to GitHub:**
  - Go to GitHub. Navigate to Settings → SSH and GPG keys → New SSH key.
  - Paste your copied key into the "Key" field and give it a relevant title. Save the key.

### 4. Clone the Repository

- **Clone Using SSH:** Find the "SSH" clone URL on the repository page. It should look like this: `git@github.com:username/repo.git`.
- **Run Clone Command:**

  ```bash
  git clone git@github.com:username/repo.git
  ```

  Replace `git@github.com:username/repo.git` with your repository's SSH URL.

## Advance Git

### Reflog

### Interactive Changes
