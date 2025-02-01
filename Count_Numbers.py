while True:
    kol_vo = []
    ga = 0
    e = 0
    a = 0
    g = 0
    def pro_ver_ka_numbers():
        global kol_vo
        global ga
        if sum(kol_vo) > 4:ga += 1
    def print_number():
        global g
        l = 0
        g1 = str(g)
        g1 = list(g1)
        while l <= len(g1) - 2:
            if l >= 3:l += 4
            if l < 3:l += 3
            g1.insert(-l, ' ')
            if g1[0] == ' ':g1.pop(0)
        u = ''.join(g1)
        print(f'  Шагов  {u}')
    def input_int(st):
        global e
        global a
        a = 0
        e = 0
        while len(st) != e:
            if st[0] == '-' and len(st) != 1:
                if e == 0:a -= 1
            if st[e] == '0':pass
            elif st[e] == '1':pass
            elif st[e] == '2':pass
            elif st[e] == '3':pass
            elif st[e] == '4':pass
            elif st[e] == '5':pass
            elif st[e] == '6':pass
            elif st[e] == '7':pass
            elif st[e] == '8':pass
            elif st[e] == '9':pass
            else: a += 1
            e += 1
        if len(st) == 0:a += 1
        if a == 0 and len(st) != 0:st = int(st)
        else:
            print('Ошибка!')
    def print_kol_vo():
        global n
        n = 0
        d = 0
        p = []
        pro_ver_ka_numbers()
        while n != len(kol_vo):
            if d == 3:
                d = 0
                p.append('.')
            p.append(kol_vo[n])
            n += 1
            d += 1
        p.reverse()
        n = 0
        da = list()
        while n != len(p):
            da.append(p[n])
            n += 1
        n = 0
        while n != len(da):
            da[n] = str(da[n])
            n += 1
        da = ''.join(da)
        print(f'{da}', end= '')
        print_number()
    kol_vo = 0
    min_s = 0
    max_s = 0
    def pro_ver_ka():
        global kol_vo
        global max_s
        global min_s
        kol_vo = 0
        max_s = input('Напишите максимальное число: ')
        input_int(max_s)
        while a != 0:
            max_s = input('Напишите максимальное число: ')
            input_int(max_s)
        else:max_s = int(max_s)
        min_s = input('Напишите минимальное число: ')
        input_int(min_s)
        while a != 0:
            min_s = input('Напишите минимальное число: ')
            input_int(min_s)
        else:min_s = int(min_s)
        if min_s >= max_s:
            print('Ошибка!')
            pro_ver_ka()
        else:min_s = str(min_s)
    pro_ver_ka()
    def kol():
        global kol_vo
        kol_vo = input('Напишите количество элементов: ')
        input_int(kol_vo)
        while a != 0:
            kol_vo = input('Напишите количество элементов: ')
            input_int(kol_vo)
        else:
            kol_vo = int(kol_vo)
            if kol_vo < 1:
                print('Ошибка!')
                kol()
    y = 0
    kol()
    kol_vo_1 = kol_vo
    kol_vo = 10 ** kol_vo
    kol_vo = str(kol_vo)
    kol_vo = kol_vo.split('0')
    kol_vo.pop(0)
    sum_kol_vo = len(kol_vo)
    while sum_kol_vo != y:
        kol_vo.pop(y)
        kol_vo.insert(y,min_s)
        y += 1
    y = len(kol_vo)-1
    while y != -1:
        kol_vo[y] = int(kol_vo[y])
        y -= 1
    min_s = int(min_s)
    maximum_ = max_s * kol_vo_1
    n = min_s
    max_s += 1
    y = 0
    while sum(kol_vo) != maximum_:
        g += 1
        n = 0
        y += 1
        print_kol_vo()
        x = 1
        kol_vo[0] += 1
        if kol_vo[0] == max_s:
            kol_vo[0] = min_s
            kol_vo[1] +=1
            while x != kol_vo_1-1:
                if kol_vo[x] == max_s:
                    kol_vo[x] = min_s
                    kol_vo[x+1] += 1
                x += 1
    g += 1
    print_kol_vo()
