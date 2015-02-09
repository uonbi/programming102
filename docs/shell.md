# Introduction to Linux (Bash) Shell
>Content adopted from *Beginning Ubuntu Linux, 5th Ed.*

> **Why Learning Linux is Important?** - check [A2A here on Quora](http://www.quora.com/How-practical-would-it-be-for-me-as-a-computer-science-student-to-learn-Linux-programming)

You can start the shell in a number of ways. The most common is to use a terminal emulator program. As its name suggests, this runs a shell inside a program window on your Desktop; by clicking Applications > Accessories > Terminal or `ctr + alt + T` keyboard combination.

Below this is the most important component of the terminal window: *the command prompt* — a few words followed by the dollar symbol ($). On our test system, this is what we see:
```
prof@prof:~$
```

>**Note:** The first part is the username—the user account we created during installation and use to log in to the PC. After the @ sign is the hostname of the PC, which we also chose when installing Ubuntu. The hostname of the PC isn’t important on most home systems, but assumes relevance if the PC is part of a network. The @ sign tells us that we are running user `prof` on the computer with the hostname `prof`.

After the colon is the current directory you’re browsing. In this example, the tilde symbol (~) appears instead of an actual path or directory name. This is merely Linux shorthand for the user’s `/home` directory.

>**Note:** If you were to log in as root, a hash (#) would appear instead of the $ prompt. This is important to remember, because often in magazines and some computer manuals, the use of the hash symbol before a command indicates that it should be run as root

##Running Programs ##
When we refer to *commands* at the shell, we’re actually talking about small programs. When you type a command to list a directory, for example, you’re starting a small program that will do that job.

The information about where your programs are stored and therefore where Ubuntu should look for commands you type in, as well as any programs you might want to run, is stored in the `PATH` variable.You can take a look at what’s currently stored there by typing the following:

```bash
echo $PATH
```

On our test PC, this returned the following information:
```bash
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

But what if you want to run a program that is not contained in a directory listed in your PATH? In this case, you must tell the shell exactly where the program is. For example:
```
./myprogram
```
So, just enter a dot and a forward slash, followed by the program name. The dot tells BASH that what you’re referring to is “right here.” Like the tilde symbol (~) mentioned earlier, this dot is BASH
shorthand.

##Getting Help ##
Each command usually has help built in, which you can query. This will explain what the command does and how it should be used. For example, you can get some instant help on the ifconfig command by
typing this:
```bash
ifconfig --help
```
In addition, most commands have technical manuals that you can read to gain a fairly complete understanding of how they work. Virtually every Ubuntu setup has a set of these man pages, which can be accessed by typing this:
```bash
man <command>
```
However, man pages are often designed for experienced Ubuntu users who understand the terminology. Some commands also have info pages, which offer slightly simpler guides. You can read these by typing this:
```bash
info <command>
```

##Working with Files ##

###Listing Files ###
Possibly the most fundamentally useful BASH command is `ls`. This lists the files in the current directory.

Having the files scroll off the screen can be annoying, so you can cram as many as possible onto each line by typing the following:
```bash
ls -m
```

The dash after the command indicates that you’re using a command option. These are also called command-line *flags* or *switches*, and they modify how a command works.

With most commands, you can use many command options at once, as long as they don’t contradict each other. For example, you could type the following:
```bash
ls -lh
```
This tells the `ls` command to produce “long” output and also to produce “human-readable” output. The long option (-l) lists file sizes and ownership permissions, among other details.
>**Caution:** Don’t forget that case-sensitivity is vitally important in Ubuntu! Typing `ls -L` is not the same as typing `ls -l`. Each will produce different results.

###Copying Files and Directories ###
Another useful command for dealing with files is `cp`, which copies files. You can use the cp command in the following way:
```bash
cp myfile /home/ubuntu/
```
This will copy the file to the location specified. In this example, the filename and location are technically known as *arguments*. Anything that you specify a command should work with is referred to
as an argument.

One important command-line option for `cp` is `-r`. This stands for recursive and tells BASH that you want to copy a directory and its contents (as well as any directories within this directory). Most
commands that deal with files have a recursive option.

One curious trick is that you can copy a file from one place to another but, by specifying a filename in the destination part of the command, change its name. Here’s an example:
```bash
cp myfile /home/ubuntu/myfile2
```
This way of copying files is a handy way of duplicating files. By not specifying a new location in the destination part of the command, but still specifying a different filename, you effectively duplicate the file within the same directory:
```
cp myfile myfile2
```

###Moving Files and Directories ###
The mv command is similar to cp, except that rather than copying the file, the old one is effectively removed. You can move files from one directory to another, for example, like this:
```bash
mv myfile /home/ubuntu/
```
You can also use the mv command to quickly rename files:
```bash
mv myfile myfile2
```
The `mv` command can be used to move a directory in the same way as with files. However, there’s no need to use a command option to specify recursivity, as with other commands.

###Deleting Files and Directories ###
>Caution: the shell doesn’t operate any kind of Recycle Bin. After a file is deleted, it’s gone forever.

Removing a file is achieved by typing something like this:
```bash
rm myfile
```
In some instances, you’ll be asked to confirm the deletion after you issue the command. If you want to delete a file without being asked to confirm it, type the following:
```bash
rm -f myfile
```

If you try to use the rm command to remove a directory, you’ll see an error message. This is because the command needs an additional option:
```bash
rm -rf mydirectory
```

###Changing and Creating Directories ###
Another handy command is `cd`, for *change directory*. This lets you move around the file system from directory to directory. Say you’re in a directory that has another directory in it, named mydirectory2. Switching to it is easy:
```bash
cd mydirectory2
```
Getting to the parent directory:
```bash
cd ..
```
To switch to the root of the file system, you would type the following:
```bash
cd /
```

You can create directories with the `mkdir` command:
```bash
mkdir mydirectory
```

What if you want to create a new directory and, at the same time, create a new directory to contain it? Simply use the `-p` command option. The following command will create a new folder called `flowers` and, at the same time, create a directory within `/flowers` called `/daffodil`:
```bash
mkdir -p flowers/daffodil
```

###Using Autocompletion ###
The Tab key is your best friend when using the shell, because it will cause BASH to automatically complete whatever you type:

* Autocompletion with Files and Paths
* Viewing Available Options

##Using Keyboard Shortcuts ##

*Keyboard Shortcuts in BASH*

Shortcut | Description 
:------------------|:-------------------------
Left/right cursor key |Moves left/right in text
Ctrl+A | Moves to beginning of line 
Ctrl+E | Moves to end of line
Ctrl+right | arrow Moves forward one word
Ctrl+left | arrow Moves left one word
 | 
 Ctrl+U | Deletes everything behind cursor to start of line
Ctrl+K | Deletes from cursor to end of line
Ctrl+W | Deletes from cursor to beginning of word
Alt+D | Deletes from cursor to end of word
Ctrl+T | Transposes characters on left and right of cursor
Alt+T | Transposes words on left and right of cursor
Ctrl+L | Clears screen (everything above current line)
Ctrl+U | Undoes everything since last command a
Alt+R | Undoes changes made to the line b
Ctrl+Y | Undoes deletion of word or line caused by using Ctrl+K, Ctrl+W, and so on c
Alt+L | Lowercases current word (from the cursor to end of word)
