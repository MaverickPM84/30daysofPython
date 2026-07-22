""" 
Question: Please concatenate this file with this one to a single text file. The content of the output file should look like below.

Expected output: 

x,y
3,5
4,9
6,10
7,11
8,12
6,10
8,18
12,20
14,22
16,24

Hint 1: Use pandas  to open the two files as data frames and the concat  method to concatenate the data frames.


Hint 2: Once you have loaded the files with pandas.read_csv  and concatenated with concat , use the to_csv  method with index=None  to export to a new file.

https://pythonhow.com/media/data/sampledata.txt

https://pythonhow.com/media/data/sampledata_x_2.txt

"""
import pandas as pd


url1 = 'https://pythonhow.com/media/data/sampledata.txt'

url2 = 'https://pythonhow.com/media/data/sampledata_x_2.txt'

data_1 = pd.read_csv(url1)

data_2 = pd.read_csv(url2)

data = pd.concat([data_1, data_2], ignore_index=True)

data.to_csv('concat.txt', index=False)

""" 
Alternate solution if you face urllib related errors

import io
import pandas
import requests

r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

Explanation 2:

In answer 1, we passed the file URL directly into read_csv . 
The read_csv  method uses the urllib  library internally to download the file. 
In case of errors with urllib you can use the more powerful library requests library as we did above.


"""