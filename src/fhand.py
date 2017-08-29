os.chdir('logs')
twrite(col.y + '\nPlease enter a year and week to inject data [YYYY WW]: ' + col.x)

while True:
    try:
        raw = input()
        year, week = raw.split(' ')
        def find_file(y, w):
            for files in os.getcwd():
                glog = y + '-W' + w + 'vals.log'
                return glog
        wstr = find_file(year, week)
        os.path.isfile(wstr)
        f = open(wstr, 'r')
    
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

                    fwp = open(wstr, 'w+')
                    fwp.close()
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
fr = open(wstr, 'r')
alldata = fr.read().splitlines()
fr.close()

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

if os.stat(wstr).st_size > 0:
    xdapd = ''.join(alldata[0]) + '   ' + str(xapflo) + '\n'
    ydapd = ''.join(alldata[1]) + '   ' + str(yapflo)
    
    twrite(col.g + \
    '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

    fw = open(wstr, 'w')
    fw.truncate()
    fw.write(xdapd)
    fw.write(ydapd)
    fw.close()

elif os.stat(wstr).st_size == 0:
    xdapd = str(xapflo) + '\n'
    ydapd = str(yapflo)
    
    twrite(col.g + \
    '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

    fw = open(wstr, 'w')
    fw.truncate()
    fw.write(xdapd)
    fw.write(ydapd)
    fw.close()
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