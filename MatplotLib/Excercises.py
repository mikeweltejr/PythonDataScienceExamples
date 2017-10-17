import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([.1,.1,.9,.9])
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Exercise1')

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
ax1.plot(x,y)
ax2.plot(x,y)

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,.9,.9])
ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax1.set_xlim([0,100])
ax1.set_ylim([0,10000])
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])
ax1.plot(x,z)
ax2.plot(x,y)

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,.9,.9])
ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax1.set_xlim([0,100])
ax1.set_ylim([0,10000])
ax2.set_xlim([0,100])
ax2.set_ylim([0,200])
ax1.plot(x,z)
ax2.plot(x,y)

fig = plt.figure()
fig,axes = plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y,ls='--',color='blue')
axes[1].plot(x,z,lw='3',color='red')

fig = plt.figure()
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(4,3))

axes[0].plot(x,y,ls='--',color='blue')
axes[1].plot(x,z,lw='3',color='red')

plt.show()
