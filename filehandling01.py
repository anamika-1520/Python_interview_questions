import os

if os.path.exists('config.txt'):
    print('file exists')
else:
    print('file does not exists')