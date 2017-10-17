import matplotlib.pyplot as plt
import numpy as np

#plt.show()

x = np.linspace(0,5,11)
y = x ** 2 

print(x)
print(y)

# Functional Method
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
#plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
#plt.show()

# Object Oriented 
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
#plt.show()

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x)
axes2.set_title('2nd Plot')
axes1.set_title('Main Plot')

plt.show()
