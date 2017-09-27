# CLI

### Filesystem
`man hier` to print out man page for filesystem hierarchy  
- `/` - root dir of filesystem  
- `/bin` - user utils fundamental to both single-user and multi-user environments  
- `Home`/`User` - On machines with home dir for users  
- `/tmp` - Temporary files which may be deleted with no notice, such as by a regular job or at system boot up  
- `/usr` -  Majority of user utils and apps. Should hold only sharable, read-only data, as to be mounted by various machines running Linux.  
- `/usr/bin` - Primary directory for executable programs, common utils, apps  

#### Absolute vs. Relative paths
Absolute: must contain root `/User/Documents/projects`  
Relative: relative to current working dir `../projects`  

#### Command Line Interface (CLI)  
- **Shell:** the command line interpreter
    - `cat /etc/shells` to list the available shells
    - `echo "$SHELL"` to print your login shell  

#### Some Commands
`man bash` substitute `bash` for any other command to retrieve manual page  
`less --help` key shortcuts, command options, etc.  
`help` for builtin command help  
`which virtualenvwrapper.sh` sub file for any other to find path to that file  


[Explain shell commands](https://explainshell.com/)

