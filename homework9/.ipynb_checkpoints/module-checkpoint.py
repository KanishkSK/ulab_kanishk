import matplotlib.pyplot as plt

import numpy as np

def subplot1():
    x = np.linspace(0,10,1000)
    fig, axs = plt.subplots(1,2, figsize=(10, 6))
    axs[0].plot(x,np.cos(x))
    axs[1].plot(x,np.sin(x))
    plt.show()
    


def subplot2():
    x = np.linspace(0,10,1000)
    fig, axs = plt.subplots(2,1, figsize=(10, 6))
    axs[0].plot(x,np.cos(x))
    axs[1].plot(x,np.sin(x))
    plt.show()

subplot1()
subplot2()