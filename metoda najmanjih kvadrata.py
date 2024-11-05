import matplotlib.pyplot as plt
import numpy as np
X_vrijednosti=[1.9881, 2.3104, 2.6896, 3.9601, 4.6225, 7.84, 8.7025, 9.1809, 9.3025, 10.4329]
Y_vrijednosti=[7.5, 10, 15, 20, 25, 30, 35, 40, 42.5, 46]
XY_vrijednosti=[]
X_kvadrat_vrijednosti=np.square(X_vrijednosti)
for i in range(0, len(Y_vrijednosti)):
        b=X_vrijednosti[i]*Y_vrijednosti[i]
        XY_vrijednosti.append(b)

sum_X=sum(X_vrijednosti)
sum_Y=sum(Y_vrijednosti)
sum_XY=sum(XY_vrijednosti)
sum_X_kvadrat=sum(X_kvadrat_vrijednosti)
n=len(X_vrijednosti)
SD_unique=0
SD_collective=0
for m in X_vrijednosti:
        sigma=np.sqrt((m-np.average(X_vrijednosti))**2/(n-1))
        SD_unique=SD_unique+sigma
for p in X_vrijednosti:
        zigma=np.sqrt((p-np.average(X_vrijednosti))**2/((n-1)*n))
        SD_collective=SD_collective+zigma

k_usamljen=(np.average(XY_vrijednosti)/np.average(X_kvadrat_vrijednosti))
k_odsjecak=(n*sum_XY-sum_X*sum_Y)/((n*sum_X_kvadrat)-(sum_X)**2)
l=(sum_Y-k_odsjecak*sum_X)/n
X_reg=np.linspace(0, X_vrijednosti[-1])
Y_reg_usamljen=[k_usamljen*x for x in X_reg]
Y_reg_odsjecak=[k_odsjecak*x+l for x in X_reg]
SD_k=np.sqrt(abs((np.average(Y_vrijednosti)/np.average(X_vrijednosti))-k_usamljen**2))*np.sqrt(1/n)

plt.xlabel("log t[s]")
plt.ylabel("log s[cm]")
plt.scatter(X_vrijednosti, Y_vrijednosti)
plt.plot(X_reg, Y_reg_usamljen)
plt.show()
print(X_vrijednosti)
print(Y_vrijednosti)
print(XY_vrijednosti)
print(X_kvadrat_vrijednosti)