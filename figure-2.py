from matplotlib import pyplot
import numpy as np

y_pos = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
Age_group = np.array(["[0,10)", "[10,20)", "[20,30)", "[30,40)", "[40,50)", "[50,60)", "[60,70)", "[70,80)", "80+"])
Dontknow = np.array([0.082, 0.127, 0.317, 0.102, 0.00, 0.00, 0.00, 0.036, 0.036])
Another_Country = np.array([0.07, 0.12, 0.312, 0.01, 0.01, 0.05, 0.00, 0.01, 0.01])
Another_State = np.array([0.19, 0.12, 0.306, 0.128, 0.082, 0.097, 0.028, 0.028, 0.028])
Texas = np.array([0.14, 0.11, 0.22, 0.11, 0.000, 0.00, 0.000, 0.021, 0.021])
Newyork = np.array([0.127, 0.092, 0.191, 0.095, 0.006, 0.081, 0.00, 0.016, 0.016])
Florida = np.array([0.115, 0.095, 0.171, 0.085, 0.065, 0.077, 0.020, 0.024, 0.00])
SomewhereinPR = np.array([0.091, 0.082, 0.135, 0.080, 0.057, 0.067, 0.011, 0.018, 0.021])
Still_in_household = np.array([0.071, 0.102, 0.11, 0.102, 0.105, 0.15, 0.16, 0.13, 0.062])

pyplot.bar(y_pos + 0.2, Dontknow, width = .40, color='antiquewhite', label=Age_group)
pyplot.bar(y_pos + 0.2, Another_Country, width = .40, color='slategrey', label=Age_group)
pyplot.bar(y_pos + 0.2, Another_State, width = .40, color='mediumpurple', label=Age_group)
pyplot.bar(y_pos + 0.2, Texas, width = .40, color='green', label=Age_group)
pyplot.bar(y_pos + 0.2, Newyork, width = .40, color='peru', label=Age_group)
pyplot.bar(y_pos + 0.2, Florida, width = .40, color='cornflowerblue', label=Age_group)
pyplot.bar(y_pos + 0.2, SomewhereinPR, width = .40, color='indianred', label=Age_group)
pyplot.bar(y_pos - 0.2, Still_in_household, width = 0.40, color='dimgrey', label=Age_group)

pyplot.bar(Age_group, Another_State, width = 0, color='blue', label=Age_group)

pyplot.legend(["Dont know", "Another Country", "Another State", "Texas", "Newyork", "Florida", "Somewhere else in PR", "Still in Household/Died in 2017"])
pyplot.title("Left in 2017")
pyplot.ylabel("Proportion")
pyplot.xlabel("Age group")
pyplot.show()
