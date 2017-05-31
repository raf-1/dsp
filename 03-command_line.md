# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd : show current working dir  
 mkdir : create a directory  
 rm -r : deleting a  directory  
 touch file.txt : create a file  
 rm : deleting a file  
 mv : renaming a file  
 ls -a : listing hidden files   
 cp <path of file to be copied> <destination> : copying a file from one dir to another  
 ln -s file link : create a symbolic link  
 grep -r pattern dir :**search recursively for a pattern in dir**
---


### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >`ls`  : list all files
`ls -a`  : display all files including hidden files
`ls -l`  : list all files with long format listing
`ls -lh`  : list all files with size in a human readable format
`ls -lah`  : list all files  including hidden files with size in a human readable format
`ls -t`  : list all files with newest files first
`ls -Glp` : list all files, exclude owner name, display directories with a /

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -alt : show all files including hidden assorted by time
ls -lR : list files recursively, long format 
emacs `ls -t | head -1` : open last edited
ls -1 : display one file name per line
sed/<search pattern>/<replace patttern>/g filename : search and replace pattern
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > it allows users to execute commands which don't read from stdin and executes commands over them.
 find -name "<pattern>" | xargs -grep i -l 'python' (notice that this behaves differently without xargs. without xargs it doesnot perform grep on each file found by find but rather performs find on the list of files found by find
 find -name "<pattern>" | xargs rm (notice that this wont work without rm)

 

