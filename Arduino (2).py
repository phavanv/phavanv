#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyfirmata as pf
from time import sleep
import matplotlib.pyplot as plt
from jupyterplot import ProgressPlot


# In[2]:


board = pf.Arduino("COM6")


# In[3]:


it = pf.util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
sleep(3)


# In[4]:


board.analog[0].read()*5
board.analog[1].read()*5


# In[5]:


f = open('text.csv', 'w')
f.close()
#f.write('hello world\n')
#f.write('by pink floyd')


# In[6]:


#for i in range(10):
    #sleep(2)
   # v = board.analog[0].read()*5
   # with open('text.csv', 'a') as f:
        #f.write(str(i) + '\t' + str(i**2) + '\n')


# In[7]:


pp = ProgressPlot(plot_names=['Voltage vs Time'], x_label='Time(s)', line_names=['Voltage Line'], x_lim=[0, 20], y_lim=[0, 5])
x = []
y = []
with open('text.csv', 'w') as f:
    for i in range(20):
        sleep(1)
        v = board.analog[0].read()*5
        v2 = 5
        x.append(i)
        y.append(v)
        pp.update(v)
        f.write(str(1) + ', ' + str(v) + '\n')
        
vt = v2 - v


# In[8]:


plt.plot(x, y)
plt.ylabel('Volatage (V)')
plt.xlabel('Time (s)')
plt.title('Voltage vs Time')


# In[9]:


print(v)
print(v2)
vd = v
# voltage drop


# In[10]:


r = (((vd/v2)*1000)/(1-(vd/v2)))
print(r)
t = (((r/1000)-1)/0.00385)
print(t)


# In[11]:


pp = ProgressPlot(plot_names=['Temperature vs Time'], x_label='Time(s)', line_names=['Temperature Line'], x_lim=[0, 120], y_lim=[-40, 40])
n = []
m = []
iterations = 120
timebetween = 90
with open('text2.csv', 'w') as p:
    for i in range(iterations*2):
        if i%2 == 0:
            board.digital[2].write(1)
            sleep(0.2)
            v = board.analog[0].read()*5
            vd = v
            r = (((vd/5)*1000)/(1-(vd/5)))
            t = (((r/1000)-1)/0.00385)
            n.append(i)
            m.append(t)
            pp.update(t)
            p.write(str(1) + ', ' + str(t) + '\n')
        else:
            board.digital[2].write(0)
            sleep(timebetween)
            


# In[12]:


plt.plot(n, m, 'b.')
plt.ylabel('Temperature (*C)')
plt.xlabel('Time (s)')
plt.title('Temperature vs Time')


# In[ ]:




