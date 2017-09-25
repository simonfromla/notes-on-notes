# Executing Shell Scripts
1. Write the script
2. Give the shell permission to execute
3. Put it somewhere the shell can find it 

Scripts are saved without an extension

### Writing the script
A shell script is a file that contains ASCII text. To create a shell script, use a text editor.  
Text editor examples: vi, vim / Emacs / nano

```
#!/bin/bash
#Loop over the files with names containing space. 
#Use `${VARIABLE//PATTERN/REPLACEMENT}` construct to replace

for x in *" "*; do
  mv -- "$x" "${x// /_}"
done
```

### Setting permission
`chmod 700 filename`
700 will give private(only you) read and write execute permissions
755 - read, write, execute to everybody

### Setting path
If in directory of saved script, running `./filename` should run. Else, add directory to your $PATH.

