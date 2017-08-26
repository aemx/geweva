import matplotlib.dates as mcal
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()

twrite(col.y + '\nPlease enter a month to be graphed: ' + col.x)

while True:
    try:
        mint = int(input())
        def find_file(name):
            for files in os.getcwd():
                glog = str(name) + 'vals.log'
                return str(name)

    except ValueError:
        twrite(col.r + \
        '\nInput was not an integer. Please retry: ' + col.x)
        continue

    try:
        mstr = find_file(mint)
        fto = mstr + 'vals.log'
        os.path.isfile(fto)
        f = open(fto, 'r')

    except IOError:
        twrite(col.r + \
        '\nThe specified log was not found. Please retry: ' + col.x)
        continue

    else:
        break

alldata = f.read().splitlines()
f.close()

xdata = np.array(alldata[0].split('  '), dtype=float)
ydata = np.array(alldata[1].split('  '), dtype=float)
fdata = np.array([xdata, ydata])

if len(ydata) < 2:
    twrite(col.r + '\nInsufficient information for graphing.' + \
    'Please add more data before attempting to produce a graph.\n\n' + col.x)
    sys.exit()

xhi, xlo = np.amax(xdata), np.amin(xdata)
yhi, ylo = np.amax(ydata) + 2.5, np.amin(ydata) - 2.5

month = cal.month_name[mint]
maxis = cal.monthrange(2017, mint)[1]

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

blinx, bliny = np.linspace(xlo, maxis), eval('mi*blinx + w')

xcur = np.linspace(xlo, xhi, 5000)
ycur = eval('-amp*np.sin(2*np.pi*xcur) + (ma*xcur + w)')

xlin, ylin = np.linspace(xlo, xhi, 50), eval('ma*xlin + w')

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
plt.axis([0, maxis, ylowest, yhighest])

graph.set_title('Weight Loss Over ' + month, fontname = 'Ubuntu Mono',
fontsize = 32, fontweight = 'bold')
graph.set_xlabel('Time', fontname = 'Ubuntu Mono', fontsize = 16)
graph.set_ylabel('Weight (lb.)', fontname = 'Ubuntu Mono', fontsize = 16)

graleg = graph.legend((lideal, lamove, lalini),
('Ideal weight, linear average',
'Actual weight, moving average',
'Actual weight, linear average'))

plt.setp(graleg.texts, fontname = 'Ubuntu Mono', fontsize = 16)
plt.show()
print()