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



import sys, pathlib, subprocess

"""

"""

if len(sys.argv) < 2:
    sys.exit("Error: Please provide atleast one filename as argument")

input_files = sys.argv[1:]
files_not_found = []

for filename in input_files:
    if not pathlib.Path(filename).is_file():
        files_not_found.append("File '{}' not found".format(filename))
        continue

    line_count = subprocess.getoutput('wc -l < ' + filename)
    print("{0:40}: {1:4} lines".format(filename, line_count))

print("\n".join(files_not_found))

