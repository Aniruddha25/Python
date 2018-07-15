import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
k=input('enter the constant1')
c=input('enter the constant2')

def model(y,t):
    dydt=(-k*y)+c
    return dydt
  
#intial condition
i=input('enter the initial condition')

#time points
a=input('enter the time1')

b=input('enter the time2')
p=input('enter the value of p')


t=np.arange(a,b,((b-a)/p))
#solve ode
y=odeint(model,i,t)
g=y.ravel()#solutions in one line 
d=y.min() #minimum value of solution
e=y.max() #Maximum value of solution

#plot
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('Displacement')
plt.show()

 
 





