import json
from pprint import pprint

os.chdir('logs')
twrite(col.y + '\nPlease enter a year and week to inject data [YYYY WW]: ' + col.x)

while True:
    try:
        raw = input()
        year, week = raw.split(' ')
        def find_file(y, w):
            for files in os.getcwd():
                glog = y + '-W' + w + 'vals.json'
                return glog
        wstr = find_file(year, week)
        os.path.isfile(wstr)
        f = json.load(open(wstr))
    
    except (ValueError, IOError):
        try:
            yint = int(year)
            wint = int(week)
        
        except ValueError:
            twrite(col.r + \
            '\nThe specified log was not found. Please retry using [YYYY WW] format: ' + col.x)
            continue

        if (1 <= wint <= 53):
            twrite(col.y + '\nThe specified log was not found.\n' + col.x)
            while True:
                twrite(col.c + \
                'Would you like to create a new log for week ' + \
                week + ' of ' + year + ' ? [Y/n] ' + col.x)
                prompt = input()

                if prompt.lower() in ('yes', 'ye', 'y', ''):
                    twrite(col.c + '\nCreating new file')
                    time.sleep(0.5)
                    twrite('.')
                    time.sleep(0.7)
                    twrite('.')
                    time.sleep(0.7)
                    twrite('.\n' + col.x)

                    fwp = json.dump({}, open(wstr, 'w'))
                    time.sleep(0.5)

                    twrite(col.g + '\nSuccess! ' + wstr + ' was created.\n' + col.x)
                    break

                elif prompt.lower() in ('no', 'n'):
                    twrite(col.r + '\nExiting...\n\n' + col.x)
                    sys.exit()

                else:
                    twrite(col.r + \
                    '\nPlease respond with "yes/y" or "no/n".\n\n' + col.x)
                    continue

            break

        else:
            twrite(col.r + \
            '\nThe specified log was not found. Please retry using [YYYY WW] format: ' + col.x)
            continue

    else:
        break

wstr = find_file(year, week)
os.path.isfile(wstr)
f = json.load(open(wstr))

twrite(col.y + '\nEnter a numerical time value: ' + col.x)

while True:
    xapraw = input()

    try:
        xapflo = float(xapraw)

    except ValueError:
        twrite(col.r + \
        '\nThe specified value was not valid. Please retry: ' + col.x)
        continue

    else:
        break

twrite(col.y + '\nEnter a numerical weight value: ' + col.x)

while True:
    yapraw = input()

    try:
        yapflo = float(yapraw)

    except ValueError:
        twrite(col.r + \
        '\nThe specified value was not valid. Please retry: ' + col.x)
        continue

    else:
        break

try:
    xlist = f['time']
    xlist.extend([xapflo])
    f['time'] = xlist

    ylist = f['weight']
    ylist.extend([yapflo])
    f['weight'] = ylist

except KeyError:
    f["time"] = [xapflo]
    f["weight"] = [yapflo]

json.dump(f, open(wstr, 'w'))

twrite(col.g + \
'\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

time.sleep(1)
twrite(col.c + 'Returning to main menu')
time.sleep(0.5)
twrite('.')
time.sleep(0.7)
twrite('.')
time.sleep(0.7)
twrite('.\n' + col.x)
time.sleep(1)

os.chdir('..')