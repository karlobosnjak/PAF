import matplotlib.pyplot as plt

def grafovi(F,m):
    while True:
        if m == 0:
            print('Masa mora biti veca od 0,ponovite unos!')
        else:
            a = F / m
            print(a)
            break

    v = 0
    x = 0
    t0 = 0
    dt = 0.1
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
    print(a_lista)
    print(v_lista)
    print(x_lista)
    print(t_lista)
    


    plt.subplot(3,1,1)
    plt.plot(t_lista, a_lista)
    plt.title('a-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('akceleracija (m/s^2)')

    plt.subplot(3,1,2)
    plt.plot(t_lista, v_lista)
    plt.title('v-t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('brzina (m/s)')

    plt.subplot(3,1,3)
    plt.plot(t_lista, x_lista)
    plt.title('x_t graf')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('put (x)')

    plt.show()

grafovi(2,50)

