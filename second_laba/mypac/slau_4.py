from math import *
import tkinter as tk
from numpy import *
from copy import deepcopy


def normalize(itog):
    readOnlyText["state"] = "normal"
    readOnlyText.insert(1.0, itog)
    readOnlyText["state"] = "disable"
    return


def clear():
    global itog
    readOnlyText["state"] = "normal"
    readOnlyText.delete(1.0, tk.END)
    readOnlyText["state"] = "disable"
    itog = ''''''
    return


def check_solve(a, mn):
    global itog
    d = deepcopy(a)
    for i in range(len(d)):
        d[i].append(mn[i])
    if len(a) == linalg.matrix_rank(d) and len(a) == linalg.matrix_rank(a):
        if linalg.det(a) != 0:
            kramer(a, mn)
            inverse(a, mn)
            gause(d)
            normalize(itog)
        else:
            itog += 'Так как определитель исходной матрицы равен 0, то методами Крамера и Обратной матрицы невозможно\n'
            gause(d)
            normalize(itog)
    else:
        itog += 'Система не имеет решений\n'
    return


def gause(a):
    global itog
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
    itog += 'Решения методом Гаусса:\n'
    itog += (str(x) + '\n')
    return


def inverse(itog_matrica, mn):
    global itog
    invert = linalg.inv(itog_matrica)
    solve = matmul(invert, mn)
    for j in range(len(solve)):
        solve[j] = round(solve[j], 2)
    for i in range(len(solve)):
        if solve[i] == -0.0 or solve[i] == +0.0:
            solve[i] = 0.0
    itog += 'Решения через обратную матрицу:\n'
    itog += (str(solve) + '\n')
    return


def kramer(itog_matrica, mn):
    global itog
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
    itog += 'Решения методом крамера:\n'
    itog += (str(solve) + '\n')
    return


def calculate():
    global itog
    readOnlyText["state"] = "normal"
    readOnlyText.delete(1.0, tk.END)
    readOnlyText["state"] = "disable"
    try:
        first = [float(inp_1.get()), float(inp_2.get()), float(inp_3.get()), float(inp_1_4.get())]
        second = [float(inp_5.get()), float(inp_6.get()), float(inp_7.get()), float(inp_2_4.get())]
        third = [float(inp_9.get()), float(inp_10.get()), float(inp_11.get()), float(inp_3_4.get())]
        four = [float(inp_13.get()), float(inp_14.get()), float(inp_15.get()), float(inp_4_4.get())]
        mn = [float(inp_4.get()), float(inp_8.get()), float(inp_12.get()), float(inp_16.get())]
        itog_matrica = [first, second, third, four]
        print(itog_matrica)
        print(mn)
        check_solve(itog_matrica, mn)
    except:
        itog += 'Неверный формат входных данных.\n'
        readOnlyText["state"] = "normal"
        readOnlyText.insert(1.0, itog)
        readOnlyText["state"] = "disable"
        return


def solve_slau_4(tab):
    global itog
    global readOnlyText
    global inp_1, inp_2, inp_3, inp_4, inp_5, inp_6, inp_7, inp_8
    global inp_9, inp_10, inp_11, inp_12, inp_13, inp_14, inp_15, inp_16
    global inp_1_4, inp_2_4, inp_3_4, inp_4_4
    itog = ''''''
    text_main = tk.Label(tab, text='Решение СЛАУ', font=("Arial", 16, "bold"))
    text_main.grid(row=1, column=1, columnspan=10)
    text_1 = tk.Label(tab, text='Введите СЛАУ:', font=("Arial", 16, "bold"))
    text_1.grid(row=4, column=0, columnspan=4, sticky='w')
    inp_1 = tk.Entry(tab)
    inp_1.grid(row=5, column=0)
    text_2 = tk.Label(tab, text='X', font=("Arial", 16, "bold"))
    text_2.grid(row=5, column=1)
    readOnlyText = tk.Text(tab, state="disable")
    readOnlyText.grid(row=2, column=0, columnspan=12)
    text_3 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_3.grid(row=5, column=2)
    inp_2 = tk.Entry(tab)
    inp_2.grid(row=5, column=3)
    text_4 = tk.Label(tab, text='Y', font=("Arial", 16, "bold"))
    text_4.grid(row=5, column=4)
    text_5 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_5.grid(row=5, column=5)
    inp_3 = tk.Entry(tab)
    inp_3.grid(row=5, column=6)
    text_6 = tk.Label(tab, text='Z', font=("Arial", 16, "bold"))
    text_6.grid(row=5, column=7)
    text_27 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_27.grid(row=5, column=8)
    inp_1_4 = tk.Entry(tab)
    inp_1_4.grid(row=5, column=9)
    text_7 = tk.Label(tab, text='=', font=("Arial", 16, "bold"))
    text_7.grid(row=5, column=10)
    inp_4 = tk.Entry(tab)
    inp_4.grid(row=5, column=11)
    inp_5 = tk.Entry(tab)
    inp_5.grid(row=7, column=0)
    text_8 = tk.Label(tab, text='X', font=("Arial", 16, "bold"))
    text_8.grid(row=7, column=1)
    text_9 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_9.grid(row=7, column=2)
    inp_6 = tk.Entry(tab)
    inp_6.grid(row=7, column=3)
    text_10 = tk.Label(tab, text='Y', font=("Arial", 16, "bold"))
    text_10.grid(row=7, column=4)
    text_11 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_11.grid(row=7, column=5)
    inp_7 = tk.Entry(tab)
    inp_7.grid(row=7, column=6)
    text_12 = tk.Label(tab, text='Z', font=("Arial", 16, "bold"))
    text_12.grid(row=7, column=7)
    text_28 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_28.grid(row=7, column=8)
    inp_2_4 = tk.Entry(tab)
    inp_2_4.grid(row=7, column=9)
    text_13 = tk.Label(tab, text='=', font=("Arial", 16, "bold"))
    text_13.grid(row=7, column=10)
    inp_8 = tk.Entry(tab)
    inp_8.grid(row=7, column=11)
    inp_9 = tk.Entry(tab)
    inp_9.grid(row=9, column=0)
    text_14 = tk.Label(tab, text='X', font=("Arial", 16, "bold"))
    text_14.grid(row=9, column=1)
    text_15 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_15.grid(row=9, column=2)
    inp_10 = tk.Entry(tab)
    inp_10.grid(row=9, column=3)
    text_16 = tk.Label(tab, text='Y', font=("Arial", 16, "bold"))
    text_16.grid(row=9, column=4)
    text_17 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_17.grid(row=9, column=5)
    inp_11 = tk.Entry(tab)
    inp_11.grid(row=9, column=6)
    text_18 = tk.Label(tab, text='Z', font=("Arial", 16, "bold"))
    text_18.grid(row=9, column=7)
    text_29 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_29.grid(row=9, column=8)
    inp_3_4 = tk.Entry(tab)
    inp_3_4.grid(row=9, column=9)
    text_19 = tk.Label(tab, text='=', font=("Arial", 16, "bold"))
    text_19.grid(row=9, column=10)
    inp_12 = tk.Entry(tab)
    inp_12.grid(row=9, column=11)
    inp_13 = tk.Entry(tab)
    inp_13.grid(row=11, column=0)
    text_20 = tk.Label(tab, text='X', font=("Arial", 16, "bold"))
    text_20.grid(row=11, column=1)
    text_21 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_21.grid(row=11, column=2)
    inp_14 = tk.Entry(tab)
    inp_14.grid(row=11, column=3)
    text_22 = tk.Label(tab, text='Y', font=("Arial", 16, "bold"))
    text_22.grid(row=11, column=4)
    text_23 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_23.grid(row=11, column=5)
    inp_15 = tk.Entry(tab)
    inp_15.grid(row=11, column=6)
    text_24 = tk.Label(tab, text='Z', font=("Arial", 16, "bold"))
    text_24.grid(row=11, column=7)
    text_26 = tk.Label(tab, text='+', font=("Arial", 16, "bold"))
    text_26.grid(row=11, column=8)
    inp_4_4 = tk.Entry(tab)
    inp_4_4.grid(row=11, column=9)
    text_25 = tk.Label(tab, text='=', font=("Arial", 16, "bold"))
    text_25.grid(row=11, column=10)
    inp_16 = tk.Entry(tab)
    inp_16.grid(row=11, column=11)
    but = tk.Button(tab, text='Решить', font=("Arial", 16, "bold"), command=calculate).grid(row=13, column=0,columnspan=4)
    btn = tk.Button(tab, text='Очистить экран вывода', font=("Arial", 16, "bold"), command=clear).grid(row=13, column=4, columnspan=8)
