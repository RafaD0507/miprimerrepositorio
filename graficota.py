import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = 1/(1+x)

plt.figure()
plt.plot(x,y)
plt.savefig("grafiquita.png")
