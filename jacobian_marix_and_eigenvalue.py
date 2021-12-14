#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import symbols, diff


# In[45]:


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


# In[57]:


a,b,c,d,e = symbols('a b c d e', real = True)
#The value of a is V
#The value of b is T
#The value of c is I
#The value of d is R
#The value of e is F


# In[47]:


## define the ode system
## order is the same with the original code in matlab
def f1(V,T,I,R,F):
    return pv*I-dv*V-B*V*T


# In[48]:


print("T:")
print(diff(f1(a,b,c,d,e), a))
print("V:")
print(diff(f1(a,b,c,d,e), a))
print("R:")
print(diff(f1(a,b,c,d,e), a))
print("I:")
print(diff(f1(a,b,c,d,e), a))
print("v:")
print(diff(f1(a,b,c,d,e), a))

print("with value")


print("V:")
print(diff(f1(a,b,c,d,e), a).subs({a:5e+06, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("T:")
print(diff(f1(a,b,c,d,e), b).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("I:")
print(diff(f1(a,b,c,d,e), c).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("R:")
print(diff(f1(a,b,c,d,e), d).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("F:")
print(diff(f1(a,b,c,d,e), e).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))


# In[49]:


def f2(V,T,I,R,F):
    return gr*(T+R)*(1-(T+R+I)/T0)-B2*V*T+rho*R-phi*F*T


# In[50]:



a,b,c,d,e = symbols('a b c d e')

print("v:")
print(diff(f2(a,b,c,d,e), a))
print("T:")
print(diff(f2(a,b,c,d,e), b)) 
print("I:")
print(diff(f2(a,b,c,d,e), c)) 
print("R:")
print(diff(f2(a,b,c,d,e), d))
print("F:")
print(diff(f2(a,b,c,d,e), e))  

print("with value")


print("V:")
print(diff(f2(a,b,c,d,e), a).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("T:")
print(diff(f2(a,b,c,d,e), b).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("I:")
print(diff(f2(a,b,c,d,e), c).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("R:")
print(diff(f2(a,b,c,d,e), d).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("F:")
print(diff(f2(a,b,c,d,e), e).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))


# In[51]:


def f3(V,T,I,R,F):
    return B2*V*T-di*I-kn*I*F


# In[52]:


print("v:")
print(diff(f3(a,b,c,d,e), a))
print("T:")
print(diff(f3(a,b,c,d,e), b)) 
print("I:")
print(diff(f3(a,b,c,d,e), c)) 
print("R:")
print(diff(f3(a,b,c,d,e), d))
print("F:")
print(diff(f3(a,b,c,d,e), e))  

print("with value")


print("V:")
print(diff(f3(a,b,c,d,e), a).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("T:")
print(diff(f3(a,b,c,d,e), b).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("I:")
print(diff(f3(a,b,c,d,e), c).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("R:")
print(diff(f3(a,b,c,d,e), d).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("F:")
print(diff(f3(a,b,c,d,e), e).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))


# In[53]:


def f4(V,T,I,R,F): ## THIS IS R
    return phi*F*T-rho*R


# In[54]:


print("v:")
print(diff(f4(a,b,c,d,e), a))
print("T:")
print(diff(f4(a,b,c,d,e), b)) 
print("I:")
print(diff(f4(a,b,c,d,e), c)) 
print("R:")
print(diff(f4(a,b,c,d,e), d))
print("F:")
print(diff(f4(a,b,c,d,e), e))  

print("with value")


print("V:")
print(diff(f4(a,b,c,d,e), a).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("T:")
print(diff(f4(a,b,c,d,e), b).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("I:")
print(diff(f4(a,b,c,d,e), c).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("R:")
print(diff(f4(a,b,c,d,e), d).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("F:")
print(diff(f4(a,b,c,d,e), e).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))


# In[55]:


def f5(V,T,I,R,F): ## THIS IS F
    return pf*I-df*F 


# In[56]:


print("v:")
print(diff(f5(a,b,c,d,e), a))
print("T:")
print(diff(f5(a,b,c,d,e), b)) 
print("I:")
print(diff(f5(a,b,c,d,e), c)) 
print("R:")
print(diff(f5(a,b,c,d,e), d))
print("F:")
print(diff(f5(a,b,c,d,e), e))  

print("with value")


print("V:")
print(diff(f5(a,b,c,d,e), a).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("T:")
print(diff(f5(a,b,c,d,e), b).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("I:")
print(diff(f5(a,b,c,d,e), c).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("R:")
print(diff(f5(a,b,c,d,e), d).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))
print("F:")
print(diff(f5(a,b,c,d,e), e).subs({a:5283570, b: 4.218e+07, c:6.5639e+05, d:1.7534e+07, e: 3.2762}))


# gr=0.8
# pv=210
# pf=10**-5
# pc=1.2
# pb=0.52
# ps=12
# pl=4
# dv=5
# di=2
# df=2
# de=0.57
# dp=0.5
# ds=2
# dl=0.015
# B=5*10**-7
# B2=3*10**-8
# phi=0.33
# rho=2.6
# ks=0.8
# kl=0.4
# kn=2.5
# ke=5*10**-5
# Bcn=1
# Bbn=0.03
# hc=10**4
# hb=10**4
# tc=6
# tb=4
# indC = round (tc/dt+1)
# indB = round (tb/dt+1)
# 
# 

# In[58]:


import numpy as np


# In[59]:


Ja1= np.array([[-26.09,-2.64,210,0,0],
               [-1.2654,-10.0464043,-4.777120,-6.2067512,-13919400.0],
               [1.2654,0.1585071,-10.19050,0,-1640975.0],
               [0,1.0811460,0,-2.60,13919400.0],
               [0,0,1.00000000000000e-5,0,-2]])


# In[61]:


Ja1


# In[60]:


## CALCULATE EIGEVALUE
np.linalg.eig(Ja1)[0]

