# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 02:17:49 2016

@author: AB Sanyal
"""

import matplotlib.pyplot as plt
import numpy as np
import math

number_nuclei = 5000
steps = 100
halflife = 50

chance = math.log(2) / halflife
nuclei = []
total = []
halflifeobs = 0

i = 1
while (i <= number_nuclei):
    nuclei.append(1)
    i += 1

total.append(sum(nuclei))

i = 1
while (i <= steps):
    j = 1
    while (j <= number_nuclei):
        r = np.random.uniform(0, 1)
        if r <= chance:
            if nuclei[j - 1] == 1:
                nuclei[j - 1] = 0
        if sum(nuclei) == number_nuclei/2:
            halflifeobs = i
        j += 1
    if (i % 10) == 0:
        print(str(i) + " time steps completed.")
    total.append(sum(nuclei))
    i += 1

plt.plot(total)
print("Half life is " + str(halflifeobs))