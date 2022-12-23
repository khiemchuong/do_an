import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()
x=np.linspace(start=-5,stop=5,num=500)
def ham_bac_4(a,b,c,d,g,x):
    f=a*x**4+b*x**3+c*x**2+d*x+g
    return f
def ham_bac_3(b,c,d,g,x):
    f = b*x**3+c*x**2+d*x+g
    return f
def ham_bac_2(c,d,g,x):
    f = c*x**2+d*x+g
    return f
def ham_bac_1(d,g,x):
    f = d*x+g
    return f
y1 = ham_bac_4(1,0,-2,0,-3,x)
y2=ham_bac_3(0,-2,0,-3,x)
y3=ham_bac_2(-2,-3,0,x)
y4=ham_bac_1(0,-3,x)
ax.plot(x,y1)
ax.plot(x,y2)
ax.plot(x,y3)
ax.plot(x,y4)
ax.set_xlabel("trục hoành-x")
ax.set_ylabel("trục tung-y")
ax.legend()
plt.show()