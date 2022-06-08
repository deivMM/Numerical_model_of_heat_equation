import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from matplotlib.animation import FuncAnimation

def calc_1D(a,b,nx,tmax,alfa,k,T0):
    m = (b-a)/nx
    x = np.linspace(0,b,nx+1)
    nt = int(tmax/0.05)
    p = tmax/nt
    lamb = alfa*p/m**2
    t = np.linspace(0,tmax,nt+1)
    u = np.zeros((nx+1, nt+1))

    u[:,0] = T0
    u[0] = 1000

    for j in range(int(nt)):
        for i in range(1,nx):
            u[i,j+1] = (1-2*lamb)*u[i,j]+lamb*(u[i+1,j]+u[i-1,j])
        u[-1,j+1] = u[-2,j+1]
    return u,t,x

def calc_1D_flux(a,b,nx,tmax,alfa,k,fa,fb,T0):
    m = (b-a)/nx
    x = np.linspace(0,b,nx+1)
    nt = int(tmax/0.05)
    p = tmax/nt
    lamb = alfa*p/m**2
    t = np.linspace(0,tmax,nt+1)
    u = np.zeros((nx+1, nt+1))
    u[:,0] = T0
    for j in range(int(nt)):
        u[0,j+1]=(1-2*lamb)*u[0,j]+2*lamb*(u[1,j]+fa*m/k)
        u[-1,j+1]=(1-2*lamb)*u[-1,j]+2*lamb*(u[-2,j]+fb*m/k)
        for i in range(1,nx):
            u[i,j+1] = (1-2*lamb)*u[i,j]+lamb*(u[i+1,j]+u[i-1,j])
    return u,t,x

def dataInt(xdata1, xdata2, ydata1, ydata2, dicr = 0.001):
    x_new1 = np.around(np.arange(xdata1.min(),xdata1.max(),dicr),3)
    x_new2 = np.around(np.arange(xdata2.min(),xdata2.max(),dicr),3)
    xnew = np.intersect1d(x_new1, x_new2)
    
    f = interp1d(xdata1, ydata1)
    ynew1 = f(xnew)
    f = interp1d(xdata2, ydata2)
    ynew2 = f(xnew)

    MSE = sum((ynew1-ynew2)**2)/len(xnew)
    return xnew, ynew1, ynew2, MSE

a = 0
b = 0.2
T0 = 20
nx = 20
tmax = 10 
density = 2700 #  density (SI-> kg/m3)
cp = 900 # Specific heat (SI-> J/kgK)
k = 40 #  thermal conductivity (SI-> W/mk)
alfa = k/(density*cp) # Thermal diffusivity (SI-> m^2/s)

############################################################

fa = 100000
fb = 0
res,t,x = calc_1D_flux(a,b,nx,tmax,alfa,k,fa,fb,T0)

fig, ax = plt.subplots()
############### ax.grid()
t_title = ax.set_title('', fontsize=15)
ax.set_xlim(0, b)
ax.set_ylim(0, 60)
line, = ax.plot(0,0, 'k')
scat = ax.scatter(0, 0, c='g',s=10)
ax.plot(x,res[:,0],'k',alpha=.2)
ax.scatter(x, res[:,0], c='k',s=10,alpha=.2)

def init():
    pass

def anim(i):
    t_title.set_text('Time: {0:.1f} sec.'.format(t[i]))
    line.set_data(x,res[:,i])
    scat.set_offsets(np.c_[x,res[:,i]])
    return line

an = FuncAnimation(fig, anim, frames=len(t), init_func=init,interval=10, repeat=False)

plt.show()
