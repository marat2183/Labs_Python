from numpy import *
from copy import deepcopy
'''
Программа решает СЛАУ 3 и 4 порядка, т.е 3 на 3 или 4 на 4.
Пример входых данных для 3 порядка:
+ 1x + 2y - 1z = 0
+ 2x - 1y + 3z = 0
+ 1x + 1y + 1z = + 1
Пример входных данных для 4 порядка:
+ 1x - 1y + 3z + 1t = + 5
+ 4x - 1y + 5z + 4t = + 4
+ 2x - 2y + 4z + 1t = + 6
+ 1x - 4y + 5z - 1t = + 3
Обязательно должны присутствовать переменные x,y,z и если 4 порядок, то t. Если в исходном уравнения какой-либо из множителей равен 0,
то записываем к примеру: + 0x - 0y + 5z - 1t = 0.
Входные данные записываются в файл: input.txt.
Каждое уравнение на отдельной строке
Выходные данные в файл: output.txt
Программа считает ответы с точностью 6 знаков после запятой.
'''

def check_solve(a, mn):
    d = deepcopy(a)
    for i in range(len(d)):
        d[i].append(mn[i])
    if len(a) == linalg.matrix_rank(d) and len(a) == linalg.matrix_rank(a):
        if linalg.det(a) != 0:
            kramer(a, mn)
            inverse(a, mn)
            gause(d)
        else:
            with open('output.txt', 'a', encoding='utf8') as f:
                f.write(
                    'Так как определитель исходной матрицы равен 0, то методами Крамера и Обратной матрицы невозможно\n')
            gause(d)
    else:
        with open('output.txt', 'a', encoding='utf8') as f:
            f.write('Система не имеет решений\n')
    return


def modify(temp):
    try:
        itog_matrica = []
        mn = []
        for i in temp:
            rav = i.find('=')
            prom = i[:rav].strip()
            new = prom.split(' ')
            for i in range(len(new)):
                if i % 2 != 0:
                    new[i] = new[i][:-1]
            filt = []
            for i in range(0, len(new), 2):
                s = float(new[i] + new[i + 1])
                filt.append(s)
            itog_matrica.append(filt)
        for i in temp:
            m = i.split('=')
            mn.append(m[-1])
        for i in range(len(mn)):
            if len(mn[i]) > 2:
                mn[i] = mn[i][1] + mn[i][3:]
        for i in range(len(mn)):
            mn[i] = float(mn[i])
        check_solve(itog_matrica, mn)
    except:
        with open('output.txt', 'a', encoding='utf8') as f:
            f.write('Неверный формат входных данных\n')
    return


def gause(a):
    x = [0 for i in range(len(a))]
    n = len(a)
    for i in range(len(a[0])):
        if a[0][i] != 0:
            filt = i
            break
    for i in range(len(a)):
        a[i][0], a[i][filt] = a[i][filt], a[i][0]
    for k in range(1, n):
        for j in range(k, n):
            m = a[j][k - 1] / a[k - 1][k - 1]
            for i in range(0, n + 1):
                a[j][i] = a[j][i] - m * a[k - 1][i]
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] / a[i][i]
        for c in range(n - 1, i, -1):
            x[i] = x[i] - a[i][c] * x[c] / a[i][i]
    for i in range(len(x)):
        if x[i] == -0.0 or x[i] == +0.0:
            x[i] = 0.0
    for i in range(len(x)):
        x[i] = round(x[i], 2)
    x[0], x[filt] = x[filt], x[0]
    with open('output.txt', 'a', encoding='utf8') as f:
        f.write('Решения методом Гаусса:\n')
        f.write(str(x) + '\n')
    return


def inverse(itog_matrica, mn):
    invert = linalg.inv(itog_matrica)
    solve = matmul(invert, mn)
    for j in range(len(solve)):
        solve[j] = round(solve[j], 2)
    for i in range(len(solve)):
        if solve[i] == -0.0 or solve[i] == +0.0:
            solve[i] = 0.0
    with open('output.txt', 'a', encoding='utf8') as f:
        f.write('Решения через обратную матрицу:\n')
        f.write(str(solve) + '\n')
    return


def kramer(itog_matrica, mn):
    solve = []
    opredelitel = round(linalg.det(itog_matrica), 6)
    for i in range(len(itog_matrica)):
        pr = copy(itog_matrica)
        pr[:, i] = mn
        op = round(linalg.det(pr), 6)
        solve.append(op / opredelitel)
    for i in range(len(solve)):
        if solve[i] == -0.0 or solve[i] == +0.0:
            solve[i] = 0.0
    for i in range(len(solve)):
        solve[i] = round(solve[i], 2)
    with open('output.txt', 'a', encoding='utf8') as f:
        f.write('Решения методом крамера:\n')
        f.write(str(solve) + '\n')
    return

temp = []
with open('output.txt', 'w', encoding='utf8') as f:
    pass
with open('input.txt', 'r', encoding='utf8') as f:
    for i in f.readlines():
        temp.append(i)
# temp = ['+ 3x - 2y + 4z = + 21','+ 3x + 4y - 2z = + 9','+ 2x - 1y - 1z = + 10']
modify(temp)

