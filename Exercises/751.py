import pandas
import pylab as plt

data = pandas.read_csv("https://pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

""" 
Explanation 1:

This solution uses the pylab library, which needs to be installed with pip install pylab . 
The solution has a few lines of code and uses the integrated pandas plot method. 
Instead of scatter , you can specify other types of plots such as line , bar , etc.


"""