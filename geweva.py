import calendar as cal
import matplotlib.dates as mcal
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns; sns.set()
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

twrite(col.g + 'Geweva Plotter ' + col.d + '[0.0.1-a7]\n\n' + col.x + \
col.c + 'Please select an operation:\n' + col.x + \
col.y + '    [0] Graph one month of data\n' + col.x + \
col.y + '    [1] Inject new data\n' + col.x + \
col.y + '    [9] Exit Geweva Plotter\n\n' + col.x)

while True:
    try:
        twrite('>>> ')
        selectop = int(input())

    except ValueError or (selectop is not [0, 1, 9]):
        twrite(col.r + '\nIncorrect operation specified. Please retry.\n\n' + col.x)
        continue
    
    else:
        break

if selectop is 0:
    twrite(col.y + '\nPlease enter a month to be graphed: ' + col.x)

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

        try:
            mstr = find_file(mint)
            fto = mstr + 'vals.log'
            os.path.isfile(fto)
            f = open(fto, 'r')

        except IOError:
            twrite(col.r + '\nThe specified Geweva log was not found. Please retry: ' + col.x)
            continue

        else:
            break

    alldata = f.read().splitlines()
    f.close()

    xdata = np.array(alldata[0].split('  '), dtype=float)
    ydata = np.array(alldata[1].split('  '), dtype=float)

    if len(ydata) < 2:
        twrite(col.r + '\nInsufficient information for graphing. Please add more data before attempting to produce a graph.\n\n' + col.x)
        sys.exit()

    xhi = np.amax(xdata)
    xlo = np.amin(xdata)
    yhi = np.amax(ydata) + 2.5
    ylo = np.amin(ydata) - 2.5

    month = cal.month_name[mint]
    maxis = cal.monthrange(2017, mint)[1]

    xply = np.polyfit(xdata, ydata, xhi)
    yply = np.poly1d(xply)
    xlin = np.polyfit(xdata, ydata, 1)
    ylin = np.poly1d(xlin)

    xnew = np.linspace(xlo, xhi, 300)
    xalt = np.linspace(xlo, xhi, 50)
    ynew = yply(xnew)
    yalt = ylin(xalt)

    blinx = np.linspace(xlo, maxis, 50)
    bliny = eval('-5*blinx/19 + 203')
    
    if np.amax(bliny) + 2.5 > yhi:
        yhighest = np.amax(bliny) + 2.5
        
    else:
        yhighest = yhi
    
    if np.amin(bliny) - 2.5 < ylo:
        ylowest = np.amin(bliny) - 2.5

    else:
        ylowest = ylo
    
    twrite(col.c + '\nGraphing data')
    time.sleep(0.5)
    twrite('.')
    time.sleep(0.7)
    twrite('.')
    time.sleep(0.7)
    twrite('.\n\n' + col.x)
    time.sleep(0.5)

    # dates = mcal.date2num('2017-' + mstr + '-1', '2017-' + mstr + '-' + str(maxis))

    fig, graph = plt.subplots()
    graph.fill_between(blinx, bliny - 2.5, bliny + 2.5, color = 'b', alpha = 0.05)
    lideal, = graph.plot(blinx, bliny, 'b')
    lamove, = graph.plot(xnew, ynew, 'g')
    lalini, = graph.plot(xalt, yalt, 'g--')
    graph.plot(xdata, ydata, 'go', markersize = 7, alpha = 0.15)
    
    plt.axis([0, maxis, ylowest, yhighest])
    graph.set_title('Weight Loss Over ' + month, fontname = 'Ubuntu Mono', fontsize = 32, fontweight = 'bold')
    graph.set_xlabel('Time', fontname = 'Ubuntu Mono', fontsize = 16)
    graph.set_ylabel('Weight (lb.)', fontname = 'Ubuntu Mono', fontsize = 16)
    graleg = graph.legend((lideal, lamove, lalini), ('Ideal weight, linear average', 'Actual weight, moving average', 'Actual weight, linear average'))
    plt.setp(graleg.texts, fontname = 'Ubuntu Mono', fontsize = 16)
    plt.show()

elif selectop is 1:
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
            twrite(col.r + '\nError: Input was not a valid integer. Please retry: ' + col.x)
            continue
        
        try:
            mstr = find_file(mint)
            fto = mstr + 'vals.log'
            os.path.isfile(fto)
            fr = open(fto, 'r')

        except IOError:
            twrite(col.y + '\nThe specified Geweva log was not found. ' + col.x + \
            col.c + 'Creating new file')
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
        
        else:
            break

    mstr = find_file(mint)
    fto = mstr + 'vals.log'
    os.path.isfile(fto)
    fr = open(fto, 'r')
    alldata = fr.read().splitlines()
    fr.close()
    twrite(col.y + '\nEnter floating-point time value: ' + col.x)
    xapraw = input()

    try:
        xapflo = float(xapraw)

    except ValueError:
        twrite(col.r + '\nError: The specified value was not floating-point.\n\n' + col.x)
        sys.exit()

    twrite(col.y + '\nEnter floating-point weight value: ' + col.x)
    yapraw = input()

    try:
        yapflo = float(yapraw)

    except ValueError:
        twrite(col.r + '\nError: The specified value was not floating-point.\n\n' + col.x)
        sys.exit()

    if os.stat(fto).st_size > 0:
        xdapd = ''.join(alldata[0]) + '   ' + str(xapflo) + '\n'
        ydapd = ''.join(alldata[1]) + '   ' + str(yapflo)
        
        twrite(col.g + '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

        fw = open(fto, 'w')
        fw.truncate()
        fw.write(xdapd)
        fw.write(ydapd)
        fw.close()

    elif os.stat(fto).st_size == 0:
        xdapd = str(xapflo) + '\n'
        ydapd = str(yapflo)
        
        twrite(col.g + '\nInput (' + str(xapflo) + ', ' + str(yapflo) + ') accepted.\n\n' + col.x)

        fw = open(fto, 'w')
        fw.truncate()
        fw.write(xdapd)
        fw.write(ydapd)
        fw.close()

elif selectop is 9:
    twrite(col.r + '\nExiting...\n\n' + col.x)