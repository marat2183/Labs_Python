from math import *
import tkinter as tk
from copy import deepcopy
from numpy import *


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
        itog +='Система не имеет решений\n'
        normalize(itog)
    return


def gause(a):
    global itog
    try:
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
    except:
        itog += 'Не удалось решить с помощью метода Гаусса.\nНе удалось привести к ступенчатой структуре'
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
        first = [float(inp_1.get()), float(inp_2.get()), float(inp_3.get())]
        second = [float(inp_5.get()), float(inp_6.get()), float(inp_7.get())]
        third = [float(inp_9.get()), float(inp_10.get()), float(inp_11.get())]
        mn = [float(inp_4.get()), float(inp_8.get()), float(inp_12.get())]
        itog_matrica = [first, second, third]
        check_solve(itog_matrica, mn)
    except:
        itog += 'Неверный формат входных данных.\n'
        readOnlyText["state"] = "normal"
        readOnlyText.insert(1.0, itog)
        readOnlyText["state"] = "disable"
        return



def slau_3(tab):
    global itog
    global readOnlyText
    global inp_1,inp_2,inp_3,inp_4,inp_5,inp_6
    global inp_7, inp_8, inp_9, inp_10, inp_11, inp_12
    font_text = ("Arial", 16, "bold")
    itog = ''''''
    text_main = tk.Label(tab, text='Решение СЛАУ', font=font_text).grid(row=1, column=1, columnspan=8)
    text_1 = tk.Label(tab, text='Введите СЛАУ:',font=font_text).grid(row=3, column=0, columnspan=4, sticky='w', padx = 5)
    inp_1 = tk.Entry(tab)
    inp_1.grid(row=4,column=0)
    text_2 = tk.Label(tab, text='X',font=font_text).grid(row=4, column=1)
    readOnlyText = tk.Text(tab, state="disable")
    readOnlyText.grid(row=2, column=0, columnspan=10, padx=55)
    text_3 = tk.Label(tab, text='+',font=font_text).grid(row=4, column=2)
    inp_2 = tk.Entry(tab)
    inp_2.grid(row=4, column=3)
    text_4 = tk.Label(tab, text='Y', font=font_text).grid(row=4, column=4)
    text_5 = tk.Label(tab, text='+',font=font_text).grid(row=4, column=5)
    inp_3 = tk.Entry(tab)
    inp_3.grid(row=4, column=6)
    text_6 = tk.Label(tab, text='Z',font=font_text).grid(row=4, column=7)
    text_7 = tk.Label(tab, text='=',font=font_text).grid(row=4, column=8)
    inp_4 = tk.Entry(tab)
    inp_4.grid(row=4, column=9)
    inp_5 = tk.Entry(tab)
    inp_5.grid(row=6,column=0)
    text_8 = tk.Label(tab, text='X',font=font_text).grid(row=6, column=1)
    text_9 = tk.Label(tab, text='+',font=font_text).grid(row=6, column=2)
    inp_6 = tk.Entry(tab)
    inp_6.grid(row=6, column=3)
    text_10 = tk.Label(tab, text='Y', font=font_text).grid(row=6, column=4)
    text_11 = tk.Label(tab, text='+',font=font_text).grid(row=6, column=5)
    inp_7 = tk.Entry(tab)
    inp_7.grid(row=6, column=6)
    text_12 = tk.Label(tab, text='Z',font=font_text).grid(row=6, column=7)
    text_13 = tk.Label(tab, text='=',font=font_text).grid(row=6, column=8)
    inp_8 = tk.Entry(tab)
    inp_8.grid(row=6, column=9)
    inp_9 = tk.Entry(tab)
    inp_9.grid(row=8,column=0)
    text_14 = tk.Label(tab, text='X',font=font_text).grid(row=8, column=1)
    text_15 = tk.Label(tab, text='+',font=font_text).grid(row=8, column=2)
    inp_10 = tk.Entry(tab)
    inp_10.grid(row=8, column=3)
    text_16 = tk.Label(tab, text='Y', font=font_text).grid(row=8, column=4)
    text_17 = tk.Label(tab, text='+',font=font_text).grid(row=8, column=5)
    inp_11 = tk.Entry(tab)
    inp_11.grid(row=8, column=6)
    text_18 = tk.Label(tab, text='Z',font=font_text).grid(row=8, column=7)
    text_19 = tk.Label(tab, text='=',font=font_text).grid(row=8, column=8)
    inp_12 = tk.Entry(tab)
    inp_12.grid(row=8, column=9)
    but = tk.Button(tab, text='Решить',font=font_text, command=calculate).grid(row=10, column=0, columnspan=4)
    btn = tk.Button(tab, text='Очистить экран вывода',font=font_text, command=clear).grid(row=10, column=4, columnspan=8)
    return

