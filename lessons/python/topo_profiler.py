
# coding: utf-8

# ## Writing stand-alone Python scripts and running on a server
# 
# We start out using the Jupyter (iPython) notebooks in these lessons because they are a friendly environment to try out individual commands and write short scripts. The Jupyter notebooks, however, can only run inside their specific graphical environment. Stand-alone Python programs are text files with the extension `.py` that are run from the command line or within an IDE (Integrated Development Environment) such as Spyder. Your Python code has to be in `.py` files to run on an HPCC.
# 
# The Jupyter notebooks are valuable in the early stages of your code development workflow, where you gradually build your program by tinkering with the code and exploring the data. However, you should quickly move your prototype code into stand-alone scripts that are platform independent and better suited for version control.
# 
# Before we dive further into Python, we are going to convert the scripts we wrote in the first lesson into stand-alone Python scripts that can run from the command line. We will first run this script locally (in your own computer) before moving it to `beach.colorado.edu`, the CSDMS HPCC, and running it on a remote server with the commands you learned during the Bash lessons.
# 

# Let's look back at the script we wrote earlier that plots the West-to-East topographic profiles across our data:

# In[2]:

import numpy as np
import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')

import urllib

url = "http://bit.ly/csdms_topo"
raw_data = urllib.urlopen(url)

topo = np.loadtxt(raw_data, delimiter=',')

plt.plot(topo[0,:], hold=True, label='North')
plt.plot(topo[-1,:], 'r--', label='South')
plt.plot(topo[len(topo)/2,:], 'g:', linewidth=3, label='Mid')

plt.title('Topographic profiles')
plt.ylabel('Elevation (m)')
plt.xlabel('<-- West    East -->')
plt.legend(loc = 'lower left')

plt.savefig('profiles.png')
plt.show()

# We can convert this code into a command-line Python script in two different ways:
# 
# * Export the Jupyter notebook as a `.py` file [File -> Download As -> Python (.py)]
# * Copy the script and paste it into a simple text file (using a text editor like TextWrangler or Notepad++) and save the file with a `.py` extension
# 
# Go ahead and convert your Jupyter notebook into a `.py` file using whichever method is easier. Call your file `topo_profiler.py` and make sure that the file is in the same directory that contains the folder `data` where the file `topo.asc` is.

# In[ ]:



