import sys

args = sys.stdin.readline()

args = args.split()
arg1 = int(args[0]) + 1
arg2 = int(args[1])
count = 0

for i in range(1, arg1): 
    for j in range(1, arg1):
        if i * j == arg2:
            count = count + 1

sys.stdout.write(str(count))

