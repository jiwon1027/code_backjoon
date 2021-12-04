import matplotlib.pyplot as plt
import numpy as np
x_sin = np.arange(0,2*np.pi*6,0.1)
y_sin = x_sin * np.sin(x_sin)

x_cos = np.arange(0,2*np.pi*6,0.1)
y_cos = 20 * np.cos(x_cos)



plt.plot(x_sin,y_sin,'r-')
plt.plot(x_cos,y_cos, 'b--')

plt.show()