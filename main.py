#!/usr/bin/python

from tkinter import Label, Tk,Button, Entry
from tkinter import messagebox, font
import re

def check_pattern():
    
    pattern = re.compile(r'^((([12][0-9]|0[1-9])[\/\-]02|([12][0-9]|0[1-9]|3[01])[\/\-](0[13578]|1[02])|([12][0-9]|0[1-9]|30)[\/\-](0[469]|11))[\/\-][0-9]{2,4}|[0-9]{2,4}[\/\-](02[\/\-]([12][0-9]|0[1-9])|(0[13578]|1[02])[\/\-]([12][0-9]|0[1-9]|3[01])|(0[469]|11)[\/\-]([12][0-9]|0[1-9]|30)))$')
    fecha = text_field.get()
    if len(fecha) != 0:
        res = re.match (pattern,fecha)
        if res:
            messagebox.showinfo(message=f'{fecha}--- Formato válido', title='Resultado')
        else:
            messagebox.showinfo(message=f'{fecha}--- Formato inválido', title='Resultado')
    else: messagebox.showerror(message='Ingrese algo',title='Error')


if __name__ == '__main__':
    root = Tk()
    root.title('Validador de formato de fechas')
    root.geometry('600x300')
    label_title = Label(root,text='Validador de fechas',width=19,height=1)
    label_title['font'] = font.Font(size=13)
    label_title.place(x=150,y=0)

    text_field = Entry(root,width=20)
    text_field['font'] = font.Font(size=12)
    text_field.place(x=150,y=100)

    btn_process_date = Button(root,text='Procesar',command=check_pattern)
    btn_process_date.place(x=220,y=150)
    btn_process_date['font'] = font.Font(size=13)


    root.mainloop()
     