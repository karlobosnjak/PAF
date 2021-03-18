import matplotlib.pyplot as plt

def graf(x1,x2,y1,y2):
    x = [x1,x2]
    y = [y1,y2]
    plt.plot(x,y)
    plt.plot(x,y,'ro')
    plt.plot()
    prikaz = int(input('Ako zelite odmah prikzati graf pritisnite 1,ako zelite graf u PDFu pritisnite 2:'))
    if prikaz == 1:
        plt.show()
    elif prikaz == 2:
        ime_grafa = input('Kako zelite nazvati sliku?')
        plt.savefig(f'{ime_grafa}.pdf')

graf(1,2,-3,0.5)


