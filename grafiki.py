import matplotlib.pyplot as plt
import numpy as np

def linijas():
    ypoints = np.array(np.random.randint(100, size=(10))) 
    
    ypoints2 = np.array(np.random.randint(100, size=(10)))
    
    plt.plot(ypoints, 'o-.')
    plt.plot(ypoints2, '+:r')
    plt.show()
linijas()