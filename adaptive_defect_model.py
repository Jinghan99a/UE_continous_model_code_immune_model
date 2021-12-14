#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import exp
from math import pow
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import copy


# In[12]:


def adapdef(y,t):
    
    z=np.zeros(np.size(y))

    z[0]=pv*y[2]-dv*y[0]-B*y[0]*y[1]
    
    z[1]=gr*(y[1]+y[3])*(1-(y[1]+y[3]+y[2])/T0)-B2*y[0]*y[1]+rho*y[3]-phi*y[4]*y[1]
    z[2]=B2*y[0]*y[1]-di*y[2]-kn*y[2]*y[4]
    z[3]=phi*y[4]*y[1]-rho*y[3] ##R
    z[4]=pf*y[2]-df*y[4] ##F

    return z



# In[13]:


#Paramaters
T0 = 1e+7
pv=210
gr=0.8
B=5*10**-7
B2=3*10**-8
rho=2.6
phi=0.33
dv=5
di=2
kn=2.5
phi=0.33
rho=2.6
pf=10**-5
df=2


# In[42]:


ts = np.linspace(0., 50, 200)

initial = [5.26e+06,4.5e+07,6.4e+05,1e+07,3]
res = spi.odeint(adapdef, initial, ts)


# In[43]:


plt.rcParams['figure.figsize'] = (9.0,9.0)

ax1=plt.subplot(221)
ax1.plot(res[:, 0],res[:, 1], "*m-")

plt.grid()
plt.xlabel("viral load")
plt.ylabel("target cell")
plt.title("phase plot")
plt.legend(loc = "best")

ax2=plt.subplot(222)
ax2.plot(res[:, 0],res[:, 2], "*m-")
plt.grid()
plt.xlabel("viral load")
plt.ylabel("infected cell")
plt.title("phase plot")
plt.legend(loc = "best")


ax3=plt.subplot(223)
ax3.plot(res[:, 0],res[:, 4], "*m-")
plt.grid()
plt.xlabel("viral load")
plt.ylabel("IFN")
plt.title("phase plot")
plt.legend(loc = "best")

ax4=plt.subplot(224)
ax4.plot(res[:, 2],res[:, 4], "*m-")
plt.grid()
plt.xlabel("infected cell")
plt.ylabel("IFN")
plt.title("phase plot")
plt.legend(loc = "best")

plt.subplots_adjust(wspace = 0.3, hspace =0.3)
plt.show()


# In[ ]:




