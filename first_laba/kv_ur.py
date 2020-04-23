from math import *

'''
Программа решает квадратные уравнения:
Пример входных данных:
+ 1x2 - 1x + 0.25 = 0
Входные данные записываются в файл: input_kv_ur.txt
Выходные данные в файл: out.txt
Уравнение записывается одной строчкой в файл.
Корни уравнения будут представлены в виде списка.
Проверка осуществляется подстановкой, в файл выводятся значения полученные при подстановке.
Если все элементы списка, в файле после подстановки равны 0, значит уравнение решено верно.
'''


def check_solution(a, b, c, solve, type):
    check_s = []
    if type == 'complex':
        for i in solve:
            ch = a * (i ** 2) + b * i + c
            m = abs(ch)
            check_s.append(m)
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Проверка решения\n')
            f.write(str(check_s) + '\n')
        return
    else:
        for i in solve:
            ch = a * (i ** 2) + b * i + c
            check_s.append(ch)
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Проверка решения\n')
            f.write(str(check_s) + '\n')
        return


def universe(a, b, c):
    solve = []
    d = b ** 2 - 4 * a * c
    x1 = (-1 * b + sqrt(d)) / (2 * a)
    x2 = (-1 * b - sqrt(d)) / (2 * a)
    if x1 == x2:
        solve.append(round(x1,2))
    else:
        solve.append(round(x1,2))
        solve.append(round(x2,2))
    with open('out.txt', 'a', encoding='utf8') as f:
        f.write('Решение через дискриминант:\n')
        f.write(str(solve) + '\n')
    check_solution(a, b, c, solve, 'discr')
    return


def simple_ur(a, b, c):
    solve = []
    solve.append(round(-c / b,2))
    with open('out.txt', 'a', encoding='utf8') as f:
        f.write('Вы ввели уравнение 1 степени, т.к показатель a = 0. Его решение::\n')
        f.write(str(solve) + '\n')
    check_solution(a, b, c, solve, 'simple')
    return


def vieta(a, b, c):
    solve = []
    first_limit = -1000
    x1 = first_limit
    x2 = first_limit
    limit = 1000
    for i in range(x1, limit + 1):
        for j in range(x2, limit + 1):
            if i + j == (-1) * b and i * j == c:
                x1 = i
                x2 = j
    if x1 == first_limit and x2 == first_limit:
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write(
                'Решение по Теореме Виета не удалось, т.к либо корни нецелые числа либо они больше 1000 и меньше -1000.\n')
        universe(a, b, c)
        return
    elif x1 == x2:
        solve.append(round(x1, 2))
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Так как дискриминант больше нуля и a равна 1, решаем по Теореме Виета:\n')
            f.write(str(solve) + '\n')
        check_solution(a, b, c, solve, 'vieta')
        return
    else:
        solve.append(round(x1,2))
        solve.append(round(x2,2))
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Так как дискриминант больше нуля и a равна 1, решаем по Теореме Виета:\n')
            f.write(str(solve) + '\n')
        check_solution(a, b, c, solve, 'vieta')
        return


def kompleksnie(d, a, b, c):
    solve = []
    d1 = d * (-1)
    e = str(round((-1 * b) / (2 * a),2))
    r = '-' + str(round(sqrt(d1) / (2 * a),2))
    r1 = '+' + str(round(sqrt(d1) / (2 * a),2))
    x1 = e + r1 + 'i'
    x2 = e + r + 'i'
    string_solve = []
    string_solve.append(x1)
    string_solve.append(x2)
    solve.append(complex(float(e), float(r1)))
    solve.append(complex(float(e), float(r)))
    with open('out.txt', 'a', encoding='utf8') as f:
        f.write('Так как дискриминант меньше нуля, решениями будут комплексные числа:\n')
        f.write(str(string_solve) + '\n')
    check_solution(a, b, c, solve, 'complex')
    return


def discr(a, b, c):
    solve = []
    d = b ** 2 - 4 * a * c
    if d == 0 and a != 1:
        x = (-1) * b // (2 * a)
        solve.append(round(x,2))
        for i in range(len(solve)):
            if solve[i] == -0.0 or solve[i] == +0.0:
                solve[i] = 0.0
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Так как дискриминант больше нуля и a не равна 1, решаем через дискриминант:\n')
            f.write(str(solve) + '\n')
        check_solution(a, b, c, solve, 'discr')
        return
    elif d > 0 and a != 1:
        x1 = (-1 * b + sqrt(d)) / (2 * a)
        x2 = (-1 * b - sqrt(d)) / (2 * a)
        solve.append(round(x1,2))
        solve.append(round(x2,2))
        for i in range(len(solve)):
            if solve[i] == -0.0 or solve[i] == +0.0:
                solve[i] = 0.0
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Так как дискриминант больше нуля и a не равна 1, решаем через дискриминант:\n')
            f.write(str(solve) + '\n')
        check_solution(a, b, c, solve, 'discr')
        return
    elif d < 0 and a == 1:
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write(
                'Решение по Теореме Виета не удалось, т.к либо корни нецелые числа либо они больше 1000 и меньше -1000.\n')
        kompleksnie(d, a, b, c)
        return
    elif d < 0 and a != 1:
        kompleksnie(d, a, b, c)
        return
    else:
        vieta(a, b, c)
        return


def select_a_b_c(uravnenie):
    try:
        if '=' in uravnenie:
            raz = uravnenie.find('=')
            uravnenie = uravnenie[:raz - 1]
        a = uravnenie.split(' ')
        for i in range(len(a)):
            if i % 2 != 0:
                b = a[i].split('x')
                a[i] = b[0]
        j = 0
        ko = []
        while j + 2 <= len(a):
            ko.append(a[j:j + 2])
            j += 2
        itog = []
        for i in ko:
            itog.append(float(i[0] + i[1]))
        a = itog[0]
        b = itog[1]
        c = itog[2]
        if a == 0:
            simple_ur(a, b, c)
            return
        else:
            discr(a, b, c)
            return
    except:
        with open('out.txt', 'a', encoding='utf8') as f:
            f.write('Неверный формат входных данных.\n')
        return


with open('input_kv_ur.txt', 'r', encoding='utf8') as f:
    uravnenie = f.readline()
with open('out.txt', 'w', encoding='utf8') as e:
    pass
select_a_b_c(uravnenie)
