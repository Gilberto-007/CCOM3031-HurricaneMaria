from matplotlib import pyplot
import numpy as np

y_pos = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
Age_group = np.array(["[0,10)", "[10,20)", "[20,30)", "[30,40)", "[40,50)", "[50,60)", "[60,70)", "[70,80)", "80+"])
ACS = np.array([0.112, 0.135, 0.135, 0.13, 0.127, 0.125, 0.115, 0.075, 0.042])
Survey = np.array([0.078, 0.10, 0.125, 0.105, 0.108, 0.152, 0.158, 0.118, 0.06])

pyplot.bar(y_pos - 0.2, ACS, width = 0.40, color='indianred', label=Age_group)
pyplot.bar(y_pos + 0.2, Survey, width = .40, color='cornflowerblue', label=Age_group)
pyplot.bar(Age_group, Survey, width = 0, color='cornflowerblue', label=Age_group)
pyplot.yticks([0.00,0.04,0.08,0.12,0.16])
pyplot.title("a) Age distribution")
pyplot.ylabel("Proportion")
pyplot.xlabel("Age group")
pyplot.show()


y_pos = np.array([0, 1, 2, 3, 4, 5, 6])
Age_group = np.array(["1", "2", "3", "4", "5", "6", "7+"])
ACS = np.array([0.25, 0.32, 0.20, 0.15, 0.05, 0.03, 0.01])
Survey = np.array([0.15, 0.34, 0.23, 0.16, 0.06, 0.04, 0.03])

pyplot.bar(y_pos - 0.2, ACS, width = 0.40, color='indianred', label=Age_group)
pyplot.bar(y_pos + 0.2, Survey, width = .40, color='cornflowerblue', label=Age_group)
pyplot.bar(Age_group, Survey, width = 0, color='cornflowerblue', label=Age_group)
pyplot.yticks([0.0,0.1,0.2,0.3])
pyplot.title("b) Household size")
pyplot.legend(["ACS (2016)", "Survey"])
pyplot.xlabel("Number of people in household")
pyplot.show()
