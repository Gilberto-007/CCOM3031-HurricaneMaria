# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E9R57GgzKNL9BMv05s_c9Ybge4mzx0vi
"""

from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np


y_pos = np.array([0, 1, 2, 3, 4, 5, 6, 7])

Remoteness = np.array([ "1\n least remote", "2", "3", "4", "5", "6", "7", "8 \n most remote" ])
deaths_per_thousand = np.array([13, 11, 12, 25,18, 15.5, 17.2 , 14])


pyplot.bar(y_pos , deaths_per_thousand, width = .8, color='gray', label= Remoteness )
pyplot.bar(Remoteness, deaths_per_thousand, width = 0, color='pink', label=Remoteness)
pyplot.title(" Figure-s6")
pyplot.ylabel("Number of deaths per 1,000 people ")
pyplot.xlabel("Remoteness")
pyplot.show()