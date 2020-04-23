from tkinter import *
from tkinter import ttk
from mypac import kv, slau, slau_4


root = Tk()
root.title('Calculate')
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Квадратные уравнения')
tab_control.grid(row=0, column=0)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='СЛАУ3')
tab_control.grid(row=0, column=1)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='СЛАУ4')
tab_control.grid(row=0, column=2)
kv.run_kv(tab1)
slau.slau_3(tab2)
slau_4.solve_slau_4(tab3)
root.mainloop()

