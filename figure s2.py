import matplotlib.pyplot as plt
import numpy as np
from scipy import stats, integrate
import pandas as pd


year2010 = [['Jan', 2384], ['Feb', 2218], ['Mar', 2470], ['Apr', 2290], ['May', 2440], ['Jun', 2405], ['Jul', 2468], ['Aug', 2564], ['Sep', 2280], ['Oct', 2468], ['Nov', 2518], ['Dec', 2778]]
year2011 = [['Jan', 2714], ['Feb', 2353], ['Mar', 2755], ['Apr', 2439], ['May', 2472], ['Jun', 2446], ['Jul', 2451], ['Aug', 2443], ['Sep', 2364], ['Oct', 2484], ['Nov', 2347], ['Dec', 2632]]
year2012 = [['Jan', 2604], ['Feb', 2442], ['Mar', 2567], ['Apr', 2480], ['May', 2370], ['Jun', 2560], ['Jul', 2434], ['Aug', 2467], ['Sep', 2451], ['Oct', 2425], ['Nov', 2456], ['Dec', 2579]]
year2013 = [['Jan', 2558], ['Feb', 2361], ['Mar', 2693], ['Apr', 2301], ['May', 2381], ['Jun', 2309], ['Jul', 2462], ['Aug', 2483], ['Sep', 2457], ['Oct', 2379], ['Nov', 2254], ['Dec', 2503]]
year2014 = [['Jan', 2464], ['Feb', 2191], ['Mar', 2467], ['Apr', 2373], ['May', 2446], ['Jun', 2371], ['Jul', 2396], ['Aug', 2521], ['Sep', 2480], ['Oct', 2866], ['Nov', 2619], ['Dec', 2858]]
year2015 = [['Jan', 2711], ['Feb', 2379], ['Mar', 2395], ['Apr', 2246], ['May', 2322], ['Jun', 2118], ['Jul', 2361], ['Aug', 2250], ['Sep', 2235], ['Oct', 2376], ['Nov', 2245], ['Dec', 2486]]
year2016 = [['Jan', 2712], ['Feb', 2562], ['Mar', 2426], ['Apr', 2225], ['May', 2283], ['Jun', 2322], ['Jul', 2442], ['Aug', 2405], ['Sep', 2347], ['Oct', 2341], ['Nov', 2458], ['Dec', 2817]]
year2017 = [['Jan', 2862], ['Feb', 2295], ['Mar', 2469], ['Apr', 2357], ['May', 2376], ['Jun', 2342], ['Jul', 2342], ['Aug', 2306], ['Sep', 2887], ['Oct', 2991], ['Nov', 2571], ['Dec', 2168]]

x1, y1 = zip(*year2010) 
x2, y2 = zip(*year2011)
x3, y3 = zip(*year2012)
x4, y4 = zip(*year2013)
x5, y5 = zip(*year2014)
x6, y6 = zip(*year2015)
x7, y7 = zip(*year2016)
x8, y8 = zip(*year2017)

plt.plot(x1, y1, 'o-', label = '2010-2016', color = 'gray')
plt.plot(x2, y2, color = 'gray')
plt.plot(x3, y3, color = 'gray')
plt.plot(x4, y4, color = 'gray')
plt.plot(x5, y5, color = 'gray')
plt.plot(x6, y6, color = 'gray')
plt.plot(x7, y7, color = 'gray')
plt.plot(x8, y8, 'o', label = '2017 Official Estimates', color = 'blue')
plt.title('Figure S2')
plt.xlabel('Month')
plt.ylabel('Number of Deaths')
plt.legend()
