import matplotlib.pyplot as plt 

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]

pops = [9, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 	4, 6, 37, 44, 50, 77, 70, 94, 93]

plt.plot(years, pops, color=(255/255, 100/255, 100/255), linewidth=6.0)

plt.ylabel("Number of Medals")
plt.xlabel("Years")
plt.title("The Medals Growth in Canada between 1924-2014")

# show the chart
plt.show()