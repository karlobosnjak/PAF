from math import sin, cos, pi
import matplotlib.pyplot as plt

def jednoliko_gibanje(F,m,v,t0,dt):
    while True:
        if m == 0:
            print('Masa mora biti veca od 0,ponovite unos!')
        else:
            a = F / m
            break
    
    x = 0
    a_lista = []
    v_lista = []
    x_lista = []
    t_lista = []
    for i in range(100):
        a_lista.append(a)
        t0 += dt
        t_lista.append(t0)
        v = v + a * dt
        v_lista.append(v)
        x = x + v * dt
        x_lista.append(x)
    
    plt.subplot(2,3,1)
    plt.plot(t_lista, a_lista)
    plt.title('a-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('akceleracija (m/s^2)')

    plt.subplot(2,3,2)
    plt.plot(t_lista, v_lista)
    plt.title('v-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('brzina (m/s)')

    plt.subplot(2,3,3)
    plt.plot(x_lista, t_lista)
    plt.title('x_t graf')
    plt.xlabel('put (x)')
    plt.ylabel('vrijeme (s)')


def kosi_hitac(g,v0,t0,dt,kut,):
    kut_rad = kut * pi /180
    x = 0
    y = 0
    x_lista = []
    y_lista = []
    t_lista = []
    for i in range(100):
        t0 += dt
        t_lista.append(t0)
        x = x + v0 * cos(kut_rad) * dt
        x_lista.append(x)
        y = y + v0 * sin(kut_rad) * dt - g * (dt**2) / 2
        y_lista.append(y)

    plt.subplot(2,3,4)
    plt.plot(x_lista, y_lista)
    plt.title('x-y graf')
    plt.xlabel('pomak (m)')
    plt.ylabel('visina (m)')

    plt.subplot(2,3,5)
    plt.plot(x_lista, t_lista)
    plt.title('x-t graf')
    plt.xlabel('pomak (m)')
    plt.ylabel('vrijeme (s)')

    plt.subplot(2,3,6)
    plt.plot(t_lista, y_lista)
    plt.title('y-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('visina (m)')



