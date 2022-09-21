from sys import argv 
filename=argv 
file=open("prod_jobs.log",mode="r")
    
    
print(filename)
name = 'COMPLETED after 1'

with open('prod_jobs.log', encoding='utf-8') as f:
    for string in f:
        if name in string:
            
            
            print(string)
