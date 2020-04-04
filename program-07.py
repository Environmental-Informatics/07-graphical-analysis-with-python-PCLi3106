"""
This script is created by Pin-Ching Li (li3106) on 03/22/2020
The USGS earthquake hazard data are downloaded and applied graphic analysis
histogram, KDE plot of magnitude of earthquake are drawn
scatter plots for lat vs long, and magnitude vs depth of earthquakes are drawn
cumulative distribution plot of earthquake depth is drawn
Q-Q plot of magnitude of earthquake is drawn
File name: "all_month.csv"
The 30 days earthquake data is accessed on 03/22/2020

"""
# import modules for following application
import pandas as pd
import matplotlib.pyplot as plt
# for Q-Q plot
import scipy.stats as stats

# read the file as a dataframe by read_table()
Earthquake = pd.read_table('all_month.csv', sep=',')

# Generate histogram of data using bin width =1, range from 0 to 10
plt.hist(Earthquake.mag,range=(0,10),rwidth=1)
plt.ylabel('numbers of data')
plt.xlabel('magnitude of earthquake')
plt.show()

# Generate KDE plot of data
Earthquake.mag.plot.kde(bw_method=.5) # Gaussian Kernel, kernel width =.5
plt.xlabel('magnitude of earthquake')
plt.show()

# Plot lat vs long
plt.scatter(Earthquake.longitude,Earthquake.latitude)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Generate normalized cumulative distribtion plot of depth
# The cumulative plot is chosen to be discrete
plt.hist(Earthquake.depth, density=True, histtype='step',
                           cumulative=True)
plt.xlabel('depth of earthquake (km)')
plt.show()

# Generate a scatter plot of earthquake magnitude vs depth
plt.scatter(Earthquake.mag,Earthquake.depth)
plt.xlabel('magnitude of earthquake')
plt.ylabel('depth of earthquake (km)')
plt.show()

# Generate a quantile plot of the earthquake magnitude
Earthquake_mag = Earthquake.mag.dropna()
# Create Q-Q plot (normal distribution is chosen)
stats.probplot(Earthquake_mag, plot=plt, dist=stats.norm);
plt.show()