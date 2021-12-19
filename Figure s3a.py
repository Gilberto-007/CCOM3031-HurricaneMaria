from matplotlib import pyplot as plt
import numpy as np
x_pos = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
remotes = np.array(["1","2","3","4","5","6","7","8","9","10","11","13"])
number = np.array([0.15,0.32,0.21,0.165,0.060,0.030,0.015,0.012,0.009,0.005,0.007,0.001])
pyplot.bar(remotes,number, width = 0.75, color = 'tomato')
plt.yticks([0.0,0.1,0.2,0.3])
plt.xlabel('Household Size')
plt.ylabel('Proportion of Sample')
