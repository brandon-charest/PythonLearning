import matplotlib.pyplot as plt
import random

x = random.sample(range(1,101),10)
y = random.sample(range(1,101),10)

plt.scatter(x,y, label='scatter', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()