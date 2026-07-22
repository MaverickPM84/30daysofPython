#Plot the data in the file provided through the URL http://pythonhow.com/data/sampledata.txt

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://pythonhow.com/data/sampledata.txt'

df = pd.read_csv(url)

#plot scatter plot of the df

df.plot.scatter(x='x', y='y')

plt.show()