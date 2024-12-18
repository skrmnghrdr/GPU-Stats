#!/usr/bin/python3


"""
Todo list.
Visualize the data via appropriate graphs


Further things:
after usage, compile it via a database and sort each
information based on the first block

ex: each lane will have a date, and the rest
might be optional, when visualizing, try extract everything
date being the minimum and data as optionals

for now, extract one column from the csv
and show a line graph

install cudf and utilize the cuda cores for faster
graph generations cause brainrott

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("nvidia_gpu_stats_2024-12-17_19-59-31.csv")

power_draw = data.iloc[:, 7] #would be powerdraw. so on so forth
#clean the output, convert to float
power_draw = [float(x.strip()[:-2]) for x in power_draw]
pass
power_draw = np.array(power_draw) #convert to numpy array
"""
Index(['timestamp', ' clocks.current.graphics [MHz]',
       ' clocks.current.memory [MHz]', ' pstate', ' utilization.gpu [%]',
       ' utilization.memory [%]', ' memory.used [MiB]', ' power.draw [W]',
       ' fan.speed [%]'],
      dtype='object')
"""
data = power_draw
df = pd.DataFrame(data, columns=['Values'])
df['Index'] = df.index
sns.lineplot(data=df, x='Index', y='Values')
plt.title('PowerDraw')
plt.xlabel('Time ==>')
plt.ylabel('Wattage')
plt.grid(True)

#np.min(np_array)
#np.max(np_array)
pass

plt.show()
#todo, make the y axis values more detailed instead of incrementing up to 50