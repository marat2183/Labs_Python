from math import *
import tkinter as tk



def normalize(itog):
    readOnlyText["state"] = "normal"
    readOnlyText.insert(1.0, itog)
    readOnlyText["state"] = "disable"
    return


def discr(a, b, c):
    global itog
    solve = []
    d = float(b ** 2 - 4 * a * c)
    if d == 0 and a != 1:
        x = float((-1) * b // (2 * a))
        solve.append(round(x,2))
        for i in range(len(solve)):
            if solve[i] == -0.0 or solve[i] == +0.0:
                solve[i] = 0.0
        itog += 'Так как дискриминант больше нуля и a не равна 1, решаем через дискриминант:\n'
        itog += (str(solve) + '\n')
        check_solution(a, b, c, solve, 'discr')
        return
    elif d > 0 and a != 1:
        first = (-b + sqrt(d)) / (2 * a)
        second = (-b - sqrt(d)) / (2 * a)
        solve.append(round(first,2))
        solve.append(round(second,2))
        for i in range(len(solve)):
            if solve[i] == -0.0 or solve[i] == +0.0:
                solve[i] = 0.0

        itog += 'Так как дискриминант больше нуля и a не равна 1, решаем через дискриминант:\n'
        itog += (str(solve) + '\n')
        check_solution(a, b, c, solve, 'discr')
        return
    elif d < 0 and a == 1:
        itog += 'Решение по Теореме Виета не удалось, т.к либо корни нецелые числа либо они больше 1000 и меньше -1000.\n'
        kompleksnie(d, a, b, c)
        return
    elif d < 0 and a != 1:
        kompleksnie(d, a, b, c)
        return
    else:
        vieta(a, b, c)
        return


def check_solution(a, b, c, solve, type):
    global itog
    check_s = []
    if type == 'complex':
        for i in solve:
            ch = a * (i ** 2) + b * i + c
            m = abs(ch)
            check_s.append(m)
        itog += 'Проверка решения\n'
        itog += (str(check_s) + '\n')
        normalize(itog)
        return
    else:
        for i in solve:
            ch = float(a * (i ** 2) + b * i + c)
            check_s.append(ch)
        itog += 'Проверка решения\n'
        itog += (str(check_s) + '\n')
        normalize(itog)
        return

def universe(a, b, c):
    global itog
    solve = []
    d = float(b ** 2 - 4 * a * c)
    x1 = float((-1 * b + sqrt(d)) / (2 * a))
    x2 = float((-1 * b - sqrt(d)) / (2 * a))
    if x1 == x2:
        solve.append(round(x1,2))
    else:
        solve.append(round(x1,2))
        solve.append(round(x2,2))
    itog += 'Решение через дискриминант:\n'
    itog += (str(solve) + '\n')
    check_solution(a, b, c, solve, 'discr')
    return


def simple_ur(a, b, c):
    global itog
    solve = []
    solve.append(float(round(-c / b,2)))
    itog += 'Вы ввели уравнение 1 степени, т.к показатель a = 0. Его решение::\n'
    itog += (str(solve) + '\n')
    check_solution(a, b, c, solve, 'simple')
    return


def vieta(a, b, c):
    global itog
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
        itog += 'Решение по Теореме Виета не удалось, т.к либо корни нецелые числа либо они больше 1000 и меньше -1000.\n'
        universe(a, b, c)
        return
    elif x1 == x2:
        solve.append(round(x1, 2))
        itog += 'Так как дискриминант больше нуля и a равна 1, решаем по Теореме Виета:\n'
        itog += (str(solve) + '\n')
        check_solution(a, b, c, solve, 'vieta')
        return
    else:
        solve.append(round(x1,2))
        solve.append(round(x2,2))
        itog += 'Так как дискриминант больше нуля и a равна 1, решаем по Теореме Виета:\n'
        itog +=( str(solve) + '\n')
        check_solution(a, b, c, solve, 'vieta')
        return


def kompleksnie(d, a, b, c):
    global itog
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
    itog += 'Так как дискриминант меньше нуля, решениями будут комплексные числа:\n'
    itog += (str(string_solve) + '\n')
    check_solution(a, b, c, solve, 'complex')
    return


def clear():
    global itog
    readOnlyText["state"] = "normal"
    readOnlyText.delete(1.0, tk.END)
    readOnlyText["state"] = "disable"
    itog = ''''''
    return



def calculate():
    global itog
    readOnlyText["state"] = "normal"
    readOnlyText.delete(1.0, tk.END)
    readOnlyText["state"] = "disable"
    try:
        a = float(inp_1.get())
        b = float(inp_2.get())
        c = float(inp_3.get())
        if a == 0:
            simple_ur(a, b, c)
            return
        else:
            discr(a, b, c)
            return
    except:
        itog += 'Неверный формат входных данных.\n'
        readOnlyText["state"] = "normal"
        readOnlyText.insert(1.0, itog)
        readOnlyText["state"] = "disable"
        return

def run_kv(tab):
    global itog
    global readOnlyText
    global inp_1
    global inp_2
    global inp_3
    font_text = ("Arial", 16, "bold")
    itog = ''''''
    text_main = tk.Label(tab, text='Решение квадратных уравнений', font=font_text)
    text_main.grid(row=1, column=0, columnspan=5, sticky='w', padx = 15)
    text_1 = tk.Label(tab, text='Введите квадратное уравнение:',font=font_text).grid(row=3, column=0, columnspan=4, sticky='w', padx=10)
    inp_1 = tk.Entry(tab)
    inp_1.grid(row=5,column=0)
    text_2 = tk.Label(tab, text='X^2',font=("Arial", 16, "bold")).grid(row=5, column=1)
    readOnlyText = tk.Text(tab, state="disable")
    readOnlyText.grid(row=2, column=0, columnspan=8, padx=40)
    text_3 = tk.Label(tab, text='+',font=("Arial", 16, "bold")).grid(row=5, column=2)
    inp_2 = tk.Entry(tab)
    inp_2.grid(row=5, column=3)
    text_4 = tk.Label(tab, text='X', font=("Arial", 16, "bold")).grid(row=5, column=4)
    text_5 = tk.Label(tab, text='+',font=("Arial", 16, "bold")).grid(row=5, column=5)
    inp_3 = tk.Entry(tab)
    inp_3.grid(row=5, column=6)
    text_6 = tk.Label(tab, text='=',font=("Arial", 16, "bold")).grid(row=5, column=7)
    text_7 = tk.Label(tab, text='0',font=("Arial", 16, "bold")).grid(row=5, column=8)
    but = tk.Button(tab, text='Решить',font=font_text, command=calculate).grid(row=7, column=0, columnspan=4)
    btn = tk.Button(tab, text='Очистить экран вывода',font=font_text, command=clear).grid(row=7, column=4, columnspan=8)