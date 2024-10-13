import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
import numpy as np 

data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')

plt.title('Erfan Asheri Histogram')

plt.xlabel('Y')

plt.ylabel('X') 

plt.show()
