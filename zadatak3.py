while True:
    x1 = float(input('Unesite x1 koordinatu:'))
    y1 = float(input('Unesite y1 koordinatu:'))
    x2 = float(input('Unesite x2 koordinatu:'))
    y2 = float(input('Unesite y2 koordinatu:'))

    k = (y2-y1) / (x2-x1)
    l = k * (-x1) + y1 
    if x2 == x1:
        print('Ponovite unos!')
    else:
        print('Jednadžba pravca:{}x+{}'.format(k,l))
        break
