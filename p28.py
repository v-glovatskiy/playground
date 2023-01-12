
import os
import sys
try:
    for entry in os.scandir(sys.argv[1]):
        if entry.is_dir():
            typ = 'dir'
        elif entry.is_file():
            typ = 'file'
        elif entry.is_symlink():
            typ = 'link'
        else:
            typ = 'unknown'
        print('{name} {typ}'.format(
            name=entry.name,
            typ=typ,
        ))
except:
    print('No such folder')
