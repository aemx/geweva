import calendar as cal
import os
import sys
import time

class col:
    r = '\033[1;31m'
    g = '\033[1;32m'
    y = '\033[1;33m'
    c = '\033[1;36m'
    d = '\033[0;32m' 
    x = '\033[0m'

os.system('clear')

def twrite(tspace):
    for char in tspace:
        time.sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()

twrite(col.g + 'Geweva Plotter ' + col.d + '0.0.2\n\n' + col.x)

header = col.c + 'Please select an operation:\n' + col.x + \
col.y + '    [0] Graph one month of data\n' + col.x + \
col.y + '    [1] Inject new data\n' + col.x + \
col.y + '    [9] Exit Geweva Plotter\n' + col.x

twrite(header)

while True:
    try:
        twrite('\n>>> ')
        selectop = int(input())

    except ValueError:
        twrite(col.r + \
        '\nIncorrect operation specified. Please retry.\n' + col.x)
        continue

    if selectop is 0:
        exec(open('src/plot.py').read())
        os.system('clear')
        twrite(header)
        continue

    elif selectop is 1:
        exec(open('src/fhand.py').read())
        os.system('clear')
        twrite(header)
        continue

    elif selectop is 9:
        twrite(col.r + '\nExiting...\n\n' + col.x)
        sys.exit()
    
    else:
        twrite(col.r + \
        '\nIncorrect operation specified. Please retry.\n' + col.x)
        continue