import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,2,200)
y = np.log(x)
#y = np.exp(x)
plt.figure()
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y = f(x)')
plt.show()
