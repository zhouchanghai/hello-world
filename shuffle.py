import sys, random, fileinput

lines = [ line for line in fileinput.input()]
random.shuffle(lines)
for line in lines:
    print line,
