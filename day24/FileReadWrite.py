
#
# Read a file
#

file = open('my_file.txt')
content = file.read()
print(content)
file.close()


#
#  write
#

file = open('my_file.txt' , mode='w')
file.write("test is a test\n")
file.write("this is another test\n")
file.close()

#
# Read a file
#

with open('my_file.txt') as file:
    content = file.read()
    print(content)


with open('my_file.txt' , mode='w') as file:
    file.write("with write test \n")
