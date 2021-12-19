from matplotlib import pyplot as plt
import numpy as np
remoteness = np.array(["1:Least\n Remote","2","3","4","5","6","7","8:Most \n Remote"])
proportions = np.array([0.025, 0.07, 0.125, 0.14, 0.10, 0.16, 0.15, 0.18])
plt.bar(remoteness, proportions, width = 0.85, color = "lightslategrey")
plt.xlabel("Remoteness")
plt.ylabel("Proportion of households without consent")
plt.yticks([0.00, 0.05, 0.10, 0.15])
plt.show()
