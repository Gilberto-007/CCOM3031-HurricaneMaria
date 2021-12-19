from matplotlib import pyplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

individuals_data = pd.read_csv('individuals.csv')
hh_data = pd.read_csv('households.csv')

df = pd.DataFrame(data= individuals_data, columns = ['1','2','3','4','5','6','7','8','9','10','11','13'])

sns.boxplot(x="variable", y="value", data=pd.melt(df))

plt.show()
