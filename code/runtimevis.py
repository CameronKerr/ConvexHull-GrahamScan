# Cameron Kerr: May 9 2023 #
# Runtime testing for ConvexHull_Vis.py #

import matplotlib.pyplot as plt
import numpy as np
import timeit
import math
import random

# Sets up figure
plt.rcParams['figure.figsize'] = [10, 6]

# Generates 50 evenly spaced integers from 10 to 1000
ns = np.linspace(10, 1000, 50, dtype=int)

# Runs runtime analysis for each n in ns
ts = [timeit.timeit('ch.full_function({}, True)'.format(n), "import convexhullvis as ch",number=5)
      for n in ns]

# Plot runtime relative to n
plt.plot(ns, ts, 'ob')
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Runtime of Graham Scan Algorithm')
plt.show()
