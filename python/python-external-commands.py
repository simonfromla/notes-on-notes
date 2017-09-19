#!/usr/bin/python3
import subprocess


"""
Calling shell commands
"""
# Executing external command 'date'
subprocess.call('date')
print("\nToday's date is ", end="", flush=True) # Default False. True ensures
# message is printed out before subprocess.call
# Passing options and arguments to command
subprocess.call(['date', '-u', '+%A']) # Pass a list [] of strings for args

# another example
print("\nSearching for 'hello world'", flush=True)
subprocess.call(['grep', '-i', 'hello world', 'hello_world.py'])


"""
Shell commands with expansion
"""
# Executing command without shell expansion
print("\nNo shell expansion when shell=False", flush=True)
subprocess.call(['echo', 'Hello $USER'])

# Executing command with shell expansion
print("\nshell expansion when shell=True", flush=True)
subprocess.call('echo Hello $USER', shell=True)

# Escape quotes if part of command
print("\nSearching for 'hello world'", flush=True)
subprocess.call('grep -i \'hello world\' hello_world.py', shell=True)

"""
*Quotes need to be escaped if they clash between command string and quotes within the command itself.
*Or avoid escaping quotes by using single/double quotes alternating.
*subprocess.call doesn't expand shell wildcards or perform command substitution, etc.,
To override this, shell=True
*Entire command now passed as a string, not list of strs.
*shell=True only when you're sure of the command, else security RISK!
https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess
*Executing shell commands that incorporate unsanitized input from an untrusted source makes a program vulnerable to shell injection, a serious security flaw which can result in arbitrary command execution. For this reason, the use of shell=True is strongly discouraged in cases where the command string is constructed from external input.*
"""
# Workaround for avoiding shell=True
import os
subprocess.call(['echo', 'Hello', os.environ.get("USER")])


"""
Command outputs and redirection
.getstatusoutput(), .getoutput() is legacy.
.call(), .check_output(), .check_call() common in python<3.5
.run() for python3.5
"""
print("Getting output of 'pwd' command", flush=True)
curr_working_dir = subprocess.getoutput('pwd')
print(curr_working_dir)

# Get status and output of command executed
# Exit status other than '0' is considered as something gone wrong
# Output of getstatusoutput() is of tuple data type
ls_command = 'ls hello_world.py xyz.py'
print("\nCalling command '{}'".format(ls_command), flush=True)
(ls_status, ls_output) = subprocess.getstatusoutput(ls_command)
print("status: {}\noutput: '{}'".format(ls_status, ls_output))

# Suppress error messages if preferred
# subprocess.call() returns status of command which can be used instead
print("\nCalling command with error msg suppressed", flush=True)
ls_status = subprocess.call(ls_command, shell=True, stderr=subprocess.DEVNULL)
print("status: {}".format(ls_status))


# Beginning python 3.5, use subprocess.run()
print("\nEquivalent to subprocess.call() is subprocess.run(['ls', '-l']):")
print(subprocess.run(["ls", "-l"]))  # doesn't capture output

# Equivalent to subprocess.check_call
try:
    print("\nEquivalent to subprocess.check_call() is subprocess.run('exit 1', shell=True, check=True):")
    print(subprocess.run("exit 1", shell=True, check=True))
except subprocess.CalledProcessError as e:
    print(e)

# Equivalent to subprocess.check_output
print("\nEquivalent to subprocess.check_output() is subprocess.run(['ls', '-l', '/dev/null'], stdout=subprocess.PIPE):")
print(subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE))
