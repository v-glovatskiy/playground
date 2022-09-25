
from sys import argv
script, filename = argv


name = 'COMPLETED after 1'

 
txt = open(filename)

print ('Содержимое файла %r' % filename)
#print (txt.read())

for string in txt:
        if name in string:
            
            
            print(string)
