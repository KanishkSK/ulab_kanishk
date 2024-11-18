import matplotlib.pyplot as plt

import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator

def create3dfunction():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    X = np.arange(-10, 10, 0.1)
    Y = np.arange(-10, 10, 0.1)
    X,Y = np.meshgrid(X, Y)
    
    Z = np.sqrt(X**2 + Y**2) # cone
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


    

