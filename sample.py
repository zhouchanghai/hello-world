import sys, random, fileinput

#https://en.wikipedia.org/wiki/Reservoir_sampling
def sample_n(num, fin):
	arr = []
	n = 0
	for line in fin:
		n += 1
		if len(arr) < num:
			arr.append(line)
		else:
			idx = random.randint(0, n-1)
			if idx < num:
				arr[idx] = line
	for line in arr:
		print line,

def sample_p(num, fin):
	p = 1.0/num
	for line in fin:
		if random.random() < p:
			print line,

def sample_i(num, fin):
	n = 0
	for line in fin:
		if n == 0:
			print line,
		n = (n+1)%num
		

if len(sys.argv) < 3 or sys.argv[1] not in ("-n", "-p", "-i"):
	print "Usage:", sys.argv[0], "-n|-p|-i num [input_file]"
	print "\t-n num: sample num lines"
	print "\t-p num: sample each line by 1/num probability"
	print "\t-i num: sample one of every num lines"
	sys.exit()

option = sys.argv[1]
num = int(sys.argv[2])
fin = fileinput.input(sys.argv[3:])

if option == "-n":
	sample_n(num, fin)
elif option == "-p":
	sample_p(num, fin)
elif option == "-i":
	sample_i(num, fin)
