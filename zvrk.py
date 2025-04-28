import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
import vpython as v 
#class initial:
    #def __init__(self, I1, I3, O1, O2, O3, theta, phi, psi):
        #self.I1=I1
        #self.I2=I1
       # self.I3=I3
        #self.O1=O1
        #self.O2=O2
        #self.O3=O3
        #self.theta=np.deg2rad(theta)
        #self.phi=np.deg2rad(phi)
        #self.psi=np.deg2rad(psi)
        #self.w=self.O3*(self.I2-self.I1) 
        #self.E0=0.5*(self.I1*self.O1**2+self.I1*self.O2**2+self.I1*self.O3**2)
        #self.Lx=self.I1*self.O1
       # self.Ly=self.I2*self.O2
        #self.Lz=self.I3*self.O3
I=0.5
I3=1
O1=3
O2=0
O3=0.5
Omax=np.hypot(O1, O2)
theta=33
phi=18
psi=16
w=O3*((I3-I)/I) 
tmax=10
steps=1000
dt=tmax/steps
t=np.arange(0, tmax, dt)
Omega1=np.zeros(int(steps))
Omega2=np.zeros(int(steps))
Omega3=np.zeros(int(steps))
for i in range(int(steps)):
    Omega1[i] = Omax*np.cos(w*t[i])
    Omega2[i] = Omax*np.sin(w*t[i])
    Omega3[i] = O3
def f(y, x):
    o1 = y[0]
    o2 = y[1]
    dt01 = -w*o2
    dt02 = w*o1
    return [dt01, dt02]
y0=[O1, O2]
y=si.odeint(f, y0, t)

o1=y[:,0]
o2=y[:,1]

#reverse integracija
tback=[tmax-dt, -dt, -dt]
y0=[o1[-1], o2[-1]]
yback=si.odeint(f, y0, tback)
#print("o1=", O1, yback[-1, 0])
#print("o2=", O2, yback[-1, 1])

#prostor i grafovi
prostor = v.canvas(title="Usporedba rješenja slobodnog/simetričnog zvrka", width=1000, height=500, background = v.vector(0.8, 0.8, 0.8))
graph = v.graph(xtitle = "t/s", ytitle="ordinata", align="left")
graph1 = v.gcurve(color=v.color.cyan, label = "graf 1")
graph2 = v.gcurve(color=v.color.green, label = "graf 2")
graph3 = v.gcurve(color=v.color.red, label = "graf 3")
#graph1a = v.gdots(color=v.color.cyan, label = "točkice 1")
#graph2a = v.gdots(color=v.color.green, label = "točkice 2")
#graph3a = v.gdots(color=v.color.red, label = "točkice 3")

#simulacija
for i in range(int(steps)):
    v.rate=int(steps/tmax)
    graph1.plot(t[i], Omega1[i])
    graph2.plot(t[i], Omega2[i])
    graph3.plot(t[i], Omega3[i])
    #graph1a.plot(t[i], Omega1[i])
    #graph2a.plot(t[i], Omega2[i])
   # graph3a.plot(t[i], Omega3[i])
