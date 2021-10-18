#!/usr/bin/python

from tkinter import *
import re

fechas =['20/11/2018','30/04/2021','11-06-1976','00-03-01','31/04/2011']

def check_pattern():
    pattern = re.compile(r'^(([12][0-9]|0[1-9])[\/\-]02|([12][0-9]|0[1-9]|3[01])[\/\-](0[13578]|1[02])|([12][0-9]|0[1-9]|30)[\/\-](0[469]|11))[\/\-][0-9]{2,4}$')
    for fecha in fechas:
        res = re.match (pattern,fecha)
        if res:
            print(fecha)
        else:
            print(f'{fecha}--- Formato inválido')


if __name__ == '__main__':
    root = Tk()
    root.title('Fechas Regex')
    root.geometry('600x300')
    root.mainloop()