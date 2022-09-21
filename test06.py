

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('prod_jobs.log')
args =parser.parse_args()
#print(args)
name = 'COMPLETED after 1'

with open('prod_jobs.log', encoding='utf-8') as f:
    for string in f:
        if name in string:
            
            
            print(string)    
    
