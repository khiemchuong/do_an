import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

#1
def cau4_1():
    def ham_mat_yen_ngua(x,y):
        z=(x/3)**2-(y/2)**2
        return z
    x=np.linspace(start=-2.0,stop=2,num=2000)
    y=np.linspace(start=-2,stop=2,num=2000)
    x,y=np.meshgrid(x,y)
    z=ham_mat_yen_ngua(x,y)
    fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf=ax.plot_surface(x,y,z,cmap=cm.gist_heat_r,linewidth=0,antialiased=False)
    fig.colorbar(rosen_surf,shrink=1,aspect=5)
    plt.show()



#2
def cau4_2():
    def ham_mat_hyperbolic1(x,y):
        q=(x/3)**2+(y/5)**2-1
        return q
    def ham_mat_hyperbolic2(x,y):
        q1=-((x/3)**2+(y/5)**2-1)
        return q1
    fig,ax=plt.subplots()
    x=np.linspace(start=-10.0,stop=10.0,num=1000)
    y=np.linspace(start=-10.0,stop=10.0,num=1000)
    x,y=np.meshgrid(x,y)
    z=ham_mat_hyperbolic1(x,y)
    z1=ham_mat_hyperbolic2(x,y)
    fig,ax=plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf=ax.plot_surface(x,y,z,cmap=cm.gist_heat_r,linewidth=0,antialiased=False)
    rosen_surf=ax.plot_surface(x,y,z1,cmap=cm.gist_heat_r,linewidth=0,antialiased=False)
    ax.set_zlim(-10,10)
    fig.colorbar(rosen_surf,shrink=0.1,aspect=7)
    plt.show()

#3
def ham_mat_cau2():
    x = np.linspace(-4, 0, 2000)
    y = np.linspace(-1, 3, 2000)


    def ham_mat_cau(x,y):
        z = np.sqrt(4-(x + 2)**2-(y-1)**2)+4
        return z

    def ham_mat_cau1(x, y):
        z1 = -np.sqrt(4-(x+2)**2-(y - 1)**2)+4
        return z1

    x, y = np.meshgrid(x, y)
    # z = np.sqrt(4 - (x + 2) ** 2 - (y - 1) ** 2) + 4
    # z1 = -np.sqrt(4 - (x + 2) ** 2 - (y - 1) ** 2) + 4
    z=ham_mat_cau(x,y)
    z1=ham_mat_cau1(x,y)
    x, y = np.meshgrid(x,y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x,y,z1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    ax.plot_surface(x,y,z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    plt.show()

def main():
    cau4_1()
    cau4_2()
    ham_mat_cau2()

if __name__=='__main__':
    main()