# Introduction to Linux (Bash) Shell
>Content adopted from *Beginning Ubuntu Linux, 5th Ed.*

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



