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
print()
sys.exit()