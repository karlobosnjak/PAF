import matplotlib.pyplot as plt
from math import sin, cos, pi

def graf(v0,kut):
    kut_rad = kut * pi /180
    g = 9.81
    dt = 0.1
    t0 = 0
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
    print(t_lista)     
    print(x_lista)
    print(y_lista)

    plt.subplot(3,1,1)
    plt.plot(x_lista, y_lista)
    plt.title('x-y graf')
    plt.xlabel('pomak (m)')
    plt.ylabel('visina (m)')

    plt.subplot(3,1,2)
    plt.plot(x_lista, t_lista)
    plt.title('x-t graf')
    plt.xlabel('pomak (m)')
    plt.ylabel('vrijeme (s)')

    plt.subplot(3,1,3)
    plt.plot(t_lista, y_lista)
    plt.title('y-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('visina (m)')

    plt.show()

graf(30,45)
