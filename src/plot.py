import json
import matplotlib.dates as mcal
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()

os.chdir('logs')
twrite(col.y + \
'\nPlease enter a year and week to be graphed [YYYY WW]: ' + col.x)

while True:
    try:
        raw = input()
        rawyear, rawweek = raw.split(' ')
        truyear, truweek = rawyear.lstrip('0'), rawweek.lstrip('0')

        if len(truweek) == 1:
            revweek = '0' + truweek

        else:
            revweek = truweek

        def find_file(y, w):
            for files in os.getcwd():
                glog = y + '-W' + w + 'vals.json'
                return glog
        wstr = find_file(truyear, revweek)
        os.path.isfile(wstr)
        f = json.load(open(wstr))

    except (ValueError, IOError):
        twrite(col.r + \
        '\nThe specified log was not found.' + \
        'Please retry using [YYYY WW] format: ' + col.x)
        continue

    else:
        break

os.chdir('..')

xdata = np.array(f['time'], dtype=float)
ydata = np.array(f['weight'], dtype=float)

if len(ydata) < 2:
    twrite(col.r + '\nInsufficient information for graphing.' + \
    'Please add more data before attempting to produce a graph.\n\n' + col.x)
    sys.exit()

xhi, xlo = np.amax(xdata), np.amin(xdata)
yhi, ylo = np.amax(ydata) + 2.5, np.amin(ydata) - 2.5

mi, w = -1/5, 200

meven = (np.polyfit(xdata[0::2], ydata[0::2], 1))[0]
modd = (np.polyfit(xdata[1::2], ydata[1::2], 1))[0]
ma = np.mean([meven, modd])

corpod = len(ydata) - 1
preamp = []
for p in range(0, corpod, 2):
    res = ydata[p + 1] - ydata[p]
    preamp.append(res)
amp = np.mean(preamp) / 2

blinx = np.linspace(0, 7)
bliny = eval('mi*blinx + w')

xcur = np.linspace(0, xhi, 5000)
ycur = eval('-amp*np.sin(2*np.pi*xcur) + (ma*xcur + w)')

xlin = np.linspace(0, 7, 50)
ylin = eval('ma*xlin + w')

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

fig, graph = plt.subplots()
graph.fill_between(blinx, bliny - 2.5, bliny + 2.5, color = 'b', alpha = 0.05)
lideal, = graph.plot(blinx, bliny, 'b')
lamove, = graph.plot(xcur, ycur, 'g')
lalini, = graph.plot(xlin, ylin, 'g--')
graph.plot(xdata, ydata, 'go', markersize = 7, alpha = 0.15)
plt.axis([0, 7, ylowest, yhighest])

graph.set_title('Weight loss for week ' + truweek + ', ' + truyear,
fontsize = 32, fontweight = 'bold')
graph.set_xlabel('Time', fontsize = 16)
graph.set_ylabel('Weight (lb.)', fontsize = 16)

graleg = graph.legend((lideal, lamove, lalini),
('Ideal weight, linear average',
'Actual weight, moving average',
'Actual weight, linear average'))

plt.setp(graleg.texts, fontsize = 14)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
mng.set_window_title(truyear + '-W' + revweek)
plt.show()
print()