"""
import numpy as np
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x)** 10 + np.cos(10 + x * y) * np.cos(x)
% matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5])
plt.colorbar();
 ipythonの際に実行"""