def parse(file):
	fd = open(file)
	lines = fd.readlines()
	args = {}
	for line in lines:
		parts = line.split(":")
		args[parts[0]] = parts[1].strip()
	return args
