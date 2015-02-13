# Introduction to Git and GitHub
>Content adopted from *Andrew Burgess (2010), Getting Good with Git*

Git is a source code manager (SCM). More accurately, it’s a distributed version control system.

**Why should I use a VCS? **
* Freedom to play
* Freedom to branch
* Freedom to to share

**Other Source-code Managers Available **
* Subversion
* Mercurial
* Perforce
* Bazaar

## Configuration

### Installing Git
For Ubuntu, to install Git is simple:

```bash
sudo apt-get install git
```

Follow documentation at [git-scm.com](http://git-scm.com), for other platforms.

### Configuring Git
Execute this in your command-line:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "your-email@something"
```

## Using Git
Well, we’re finally ready to start using Git! The first step is to set up our Git repository.

### Git Init
It’s incredibly simple to start using Git on a project; just run this command from within the project directory:

```bash
$ git init
```

For the technical, notice the path in the response to the git init
command: it’s your project directory with a .git directory inside.
That .git directory is the home for all Git’s work.

### Git Status
Run this command:
```bash
$ git status
```

`git status` just like from the name, shows the status of your *repository* at any particular time; highlighting:

* Changes staged for commit
* Changes not staged for commit
* Untracked changes

### Git Add
This command tells Git to start tracking our changes (staging).

We’ll look at two ways to do this; first, we can tell Git to track all the files in the directory (and all sub-directories) by using the . (dot) parameter:

```bash
$ git add .
```

If you don’t want to add all the files, you can do them individually
by giving their names as parameters, e.g.

```bash
$ git add hello.txt hello.c
```

So, what happens when we use the git add command? Git is “moving” the files into what’s called the staging area. Think of the staging area as a loading dock: the files are ready to go, but they haven’t yet been loaded on a truck. It’s up to you to tell Git what to do with these staged files.

Check status again now:

```bash
$ git status
```

### Git Commit
The correct name for a project snapshot is a commit. The simplest way to make a commit is to execute this command:
```bash
$ git commit -m "put message here"
```

For every commit you make, you’ll supply a short message to remind you what’s in the commit. It’s a little change-log, if you will, recording the changes between this and the previous commit.

We can see more information about our commit by running the `git log` command:

```bash
$ git log
```

### Branching
Imagine this: you’re working on a project and you have an idea for a new feature. You don’t want to risk messing up the project; so, you create a new branch on your Git repository to work on the feature.

When it’s done and ready, you can merge your changes into the main
line.

Basically, branching creates a safe sandbox (identical to the main project when you start) for you to play in, where you don’t have to worry about hurting other things.

You can see the branches you have by using the command git branch.

```bash
$ git branch
```

An asterisk will precede the name of the branch we’re on. We create a branch by using the `git branch` command:

```bash
$ git branch [name-of-branch]
```

To switch to the created branch, use the `git checkout` command:

```bash
$ git checkout [name-of-branch]
```

Whatever changes were made on one branch will not be visible at all from the other branches. Since Git tracks contents, this works for files and whole directories down to lines and characters.

## Working with Remote Repositories (GitHub)
For this class, we will use GitHub, but we have other remote repository services like BitBucket, etc.

### Sign up on GitHub
It's simple, just go to [github.com](https://github.com) and sign up.

### Create Empty Repo on GitHub
Create your first repo on GitHub by clicking on the "+" next to your username, and choose *New Repository*:
* Put the name of the repository (no spaces)
* Put some description
* You can initialize with a README file, it's always good practice.

### Git Clone
To create a copy of your GitHub (remote) repository on your *local machine*, we use `git clone` command, e.g.

```bash
$ git clone https://github.com/uonbi/programming102.git
```

### Git Push
After making changes, and *committing* them, you can now update your remote repo by using `git push` i.e.

```bash
$ git push
```


> *Note: * Please note that what we've covered is just the basics, Git has a lot more. However, this is enough for now, to get us started.

## For Further Reading
* Recommended [Free Git Online Course on CodeSchool](https://www.codeschool.com/courses/try-git)
* Handling Git Conflicts
* [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* Tagging
* Git Fetch
* Using MarkDown - *for writing README files, etc*
