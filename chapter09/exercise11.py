myfile = open('myfile.txt', 'w')
myfile.write('hello file world!\n')
myfile.close()

myfile = open('myfile.txt')
myfile.readline()
myfile.close()