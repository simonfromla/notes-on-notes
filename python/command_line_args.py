# import sys

# """
# Known number of arguments
# Arguments passed to python programs are automagically saved into a `sys.argv` list
# Use `sys.ext()` to terminate the program with an error message and exit status 1
# """


# if len(sys.argv) != 3:
#     sys.exit("Error: Please provide exactly two numbers as arguments")
# else:
#     (num1, num2) = sys.argv[1:]
#     total = int(num1) + int(num2)
#     print("{} + {} = {}".format(num1, num2, total))



# import sys, pathlib, subprocess

# """
# `wc` print word, newline, or byte count
# `-l` specify line count
# `os` module if python version < 3.4
# """

# if len(sys.argv) < 2:
#     sys.exit("Error: Please provide atleast one filename as argument")

# input_files = sys.argv[1:]
# files_not_found = []

# for filename in input_files:
#     # if not os.path.isfile(filename):
#     #     sys.exit("File '{}' not found".format(filename))
#     if not pathlib.Path(filename).is_file():
#         files_not_found.append("File '{}' not found".format(filename))
#         continue

#     line_count = subprocess.getoutput('wc -l < ' + filename)
#     print("{0:40}: {1:4} lines".format(filename, line_count))

# print("\n".join(files_not_found))



# import sys, pathlib, subprocess, re

# """
# Using filename in code

# If re.searched filename exists, uses shell commands, through subprocess, to print out num lines/words
# """

# if len(sys.argv) != 2:
#     sys.exit("Error: Please provide exactly one filename as argument")

# program_name = sys.argv[0]
# filename = sys.argv[1]

# if not pathlib.Path(filename).is_file():
#     sys.exit("File '{}' not found".format(filename))

# if re.search(r'command_line_args.py', program_name):
#     lc = subprocess.getoutput('wc -l < ' + filename)
#     print("No. of lines in '{}' is: {}".format(filename, lc))
# elif re.search(r'python-external-commands.py', program_name):
#     wc = subprocess.getoutput('wc -w < ' + filename)
#     print("No. of words in '{}' is: {}".format(filename, wc))
# else:
#     sys.exit("Program name '{}' not recognized".format(program_name))
    
    

# import argparse, subprocess

# """
# Handling CLI switches with argparse module

# Takes a file and sorts the newlines alphbetically
    # -f specified as required
# """

# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '--file', help="file to be sorted", required=True)
# parser.add_argument('-u', help="sort uniquely", action="store_true")
# args = parser.parse_args()

# if args.u:
#     subprocess.call(['sort', '-u', args.file, '-o', args.file])
# else:
#     subprocess.call(['sort', args.file, '-o', args.file])
    


import argparse

"""
Specifying positional arguments
https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
Adds first arg with second arg
"""

parser = argparse.ArgumentParser()
parser.add_argument('num1', type=int, help="first number")
parser.add_argument('num2', type=int, help="second number")
args = parser.parse_args()

total = args.num1 + args.num2
print("{} + {} = {}".format(args.num1, args.num2, total))
