
from sys import argv
try:
    script, filename = argv

    name = 'COMPLETED after 1'

    txt = open(filename)
    #f.close()

    print ('Содержимое файла %r' % filename)
    #print (txt.read())

    for string in txt:
        if name in string:
            
            
            print(string)
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."


    print(msg)

