

#from binascii import b2a_qp
import sys
#список аргументов, без названия скрипта,
l = sys.argv[1:]
print(l)

name = 'COMPLETED after 1'
with open('prod_jobs.log', encoding='utf-8') as f:
    for string in f:
        if name in string:
            
            
            print(string)
