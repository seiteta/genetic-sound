# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:45:27 2016

@author: Fred
"""

import matplotlib.pyplot as plt
import numpy as np



f = 50
sample = 1600
phi = 50
x = np.arange(sample)
y = np.sin(f * x - phi)
plt.plot(x, y)
plt.show()