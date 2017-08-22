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

header = col.g + 'Geweva Plotter ' + col.x + col.d + '[2017 nodist 1, Aug 10 2017]\n\n' + col.x + \
col.c + 'Please select an operation:\n' + col.x + \
col.y + '    [0] Graph one month of data\n' + col.x + \
col.y + '    [1] Inject new data\n\n' + col.x + '>>> '

def twrite(tspace):
    for char in tspace:
        time.sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()

twrite(header)
selectop = input()

try:
    seltf = 0 <= int(selectop) <= 1
    if seltf == False:
        raise ValueError()
        
except ValueError:
    twrite(col.r + '\nError: Incorrect operation specified.\n\n' + col.x)
    sys.exit()

if int(selectop) == 0:
    twrite(col.y + '\nPlease enter a month to be graphed: ' + col.x)
    mraw = input()

    try:
        mint = int(mraw)
        def find_file(name):
            for files in os.getcwd():
                glog = str(name) + 'vals.log'
                return str(name)

    except ValueError:
        twrite(col.r + '\nError: Input was not an integer.\n\n' + col.x)
        sys.exit()

    try:
        mstr = find_file(mint)
        fto = mstr + 'vals.log'
        os.path.isfile(fto)
        f = open(fto, 'r')
        alldata = f.read().splitlines()
        f.close()

        xdata = np.array(alldata[0].split('  '), dtype=float)
        ydata = np.array(alldata[1].split('  '), dtype=float)

        if len(ydata) < 2:
            twrite(col.r + '\nError: Insufficient information for graphing.\n\n' + col.x)
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

        # Store by week rather than month   [0.1.0]
        # X-axis time                       [0.2.0]
        # Preferences/config                [0.2.1]
            # Weight loss per week
            # Uncertainty range
            # Starting weight
        # Enter range                       [0.2.2]

    except IOError:
        twrite(col.r + '\nError: The specified Geweva log was not found.\n\n' + col.x)

elif int(selectop) == 1:
    twrite(col.y + '\nPlease enter a month to inject data: ' + col.x)
    mraw = input()

    try:
        mint = int(mraw)
        def find_file(name):
            for files in os.getcwd():
                glog = str(name) + 'vals.log'
                return str(name)

    except ValueError:
        twrite(col.r + '\nError: Input was not an integer.\n\n' + col.x)
        sys.exit()

    try:
        mthtf = 1 <= mint <= 12
        if mthtf == False:
            raise ValueError()

    except ValueError:
        twrite(col.r + '\nError: Input was not a valid integer.\n\n' + col.x)
        sys.exit()

    try:
        mstr = find_file(mint)
        fto = mstr + 'vals.log'
        os.path.isfile(fto)
        fr = open(fto, 'r')
        alldata = fr.read().splitlines()
        fr.close()

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

    try:
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
    except:
        pass