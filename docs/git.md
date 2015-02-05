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
TBD...



