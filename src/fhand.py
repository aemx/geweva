twrite(col.y + '\nPlease enter a month to inject data: ' + col.x)

while True:
    try:
        mint = int(input())
        def find_file(name):
            for files in os.getcwd():
                glog = str(name) + 'vals.log'
                return str(name)

    except ValueError:
        twrite(col.r + '\nInput was not an integer. Please retry: ' + col.x)
        continue

    if not (1 <= mint <= 12):
        twrite(col.r + \
        '\nInput was not a valid integer. Please retry: ' + col.x)
        continue
    
    try:
        mstr = find_file(mint)
        fto = mstr + 'vals.log'
        os.path.isfile(fto)
        fr = open(fto, 'r')

    except IOError:
        twrite(col.y + '\nThe specified Geweva log was not found.\n' + col.x)
        while True:
            month = cal.month_name[mint]
            twrite(col.c + \
            'Would you like to create a new log for the month of ' + \
            month + '? [Y/n] ' + col.x)
            prompt = input()

            if prompt.lower() in ('yes', 'ye', 'y', ''):
                twrite(col.c + '\nCreating new file')
                time.sleep(0.5)
                twrite('.')
                time.sleep(0.7)
                twrite('.')
                time.sleep(0.7)
                twrite('.\n' + col.x)

                fwp = open(fto, 'w+')
                fwp.close()
                time.sleep(0.5)

                twrite(col.g + '\nSuccess! ' + fto + ' was created.\n' + col.x)
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
        break

mstr = find_file(mint)
fto = mstr + 'vals.log'
os.path.isfile(fto)
fr = open(fto, 'r')
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

if os.stat(fto).st_size > 0:
    xdapd = ''.join(alldata[0]) + '   ' + str(xapflo) + '\n'
    ydapd = ''.join(alldata[1]) + '   ' + str(yapflo)
    
    twrite(col.g + \
    '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

    fw = open(fto, 'w')
    fw.truncate()
    fw.write(xdapd)
    fw.write(ydapd)
    fw.close()

elif os.stat(fto).st_size == 0:
    xdapd = str(xapflo) + '\n'
    ydapd = str(yapflo)
    
    twrite(col.g + \
    '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

    fw = open(fto, 'w')
    fw.truncate()
    fw.write(xdapd)
    fw.write(ydapd)
    fw.close()