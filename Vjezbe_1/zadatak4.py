def funkcija(x1,y1,x2,y2):
    k = (y2-y1) / (x2-x1)
    l = k * (-x1) + y1 
    if x2 == x1:
        print('Ponovite unos!')
    else:
        print('Jednadžba pravca:{}x+{}'.format(k,l))


funkcija(1,2,-3,0.5)