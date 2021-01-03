


# write to a file
path = 'myfile.txt'
my_file = open(path, 'w')
title='My name is\n'
name='Sagi\n'
my_file.wrte(title)
my_file.write(name)
my_file.close()

# read from file
read_path = 'mystery.txt'
read_file = open(read_path, 'r') 
content = read_file.read()
#print(content)
read_file.close()
