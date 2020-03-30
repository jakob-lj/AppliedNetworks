import sys

command = " ".join(sys.argv[1:])

with open('/home/jakoblj/Documents/commands.dat', 'a') as f:
    f.write(command+ "\n")
