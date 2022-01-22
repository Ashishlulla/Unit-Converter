import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.geometry('400x350')
window.resizable(0, 0)
window.title("Units Converter")
window.configure(background="#dfe6e9")

# ____________________________________________Functionality _____________________________________

def action():
    unit1 = unit_1_var.get()
    unit2 = unit_2_var.get()
    value1 = value_1_var.get()
    a = 0
    if unit1 == 'millimeter':
        if unit2 == 'centimeter':
            a = str(int(value1)/10)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 10")
        elif unit2 == 'meter':
            a = str(int(value1)/10)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 1000")
        elif unit2 == 'micrometer':
            a = str(int(value1)*1000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000")
        elif unit2 == 'nanometer':
            a = str(int(value1)*1000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000000")
        elif unit2 == 'kilometer':
            a = str(int(value1)*0.000001)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 1000000")
        elif unit2 == 'mile':
            a = str(int(value1)/1609000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 1.609e+6")
        elif unit2 == 'feet':
            a = str(int(value1)/305)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 305")
        elif unit2 == 'inch':
            a = str(int(value1)/25.4)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 25.4")

# _____________________________________ Label Frame ____________________________________
label_frame = tk.LabelFrame(window, background="#dfe6e9", border=0, relief=SUNKEN)
label_frame.pack(pady=20, padx=20)

label = tk.Label(label_frame, text="UNIT CONVERTER",
                 font=("Arial", 14, 'bold', 'underline'), background="#dfe6e9", foreground="#2d3436")
label.pack(pady=20)

# ______________________________________ Units Frame_________________________________________________

units_frame = tk.LabelFrame(window, background="#dfe6e9", border=0, relief=SUNKEN)
units_frame.pack(padx=30)

unit_1_var = tk.StringVar()
unit_1 = ttk.Combobox(units_frame, textvariable=unit_1_var, state='readonly')
unit_1['values'] = ("millimeter",
                    "centimeter",
                    'meter',
                    'micrometer',
                    'nanometer',
                    'kilometer',
                    'mile',
                    'feet',
                    'inch')
unit_1.current(1)
unit_1.pack(side='left', padx=10, pady=10)

to_label = tk.Label(units_frame, text="to", bg="#dfe6e9")
to_label.pack(side='left', padx=10, pady=10)

unit_2_var = tk.StringVar()
unit_2 = ttk.Combobox(units_frame, textvariable=unit_2_var, state='readonly')
unit_2['values'] = ("millimeter",
                    "centimeter",
                    'meter',
                    'micrometer',
                    'nanometer',
                    'kilometer',
                    'mile',
                    'feet',
                    'inch')
unit_2.current(2)
unit_2.pack(side='left', padx=10, pady=10)

# ______________________________________ Values Boxes Frame_________________________________________________

box_frame = tk.LabelFrame(window, background="#dfe6e9", border=0, relief=SUNKEN)
box_frame.pack(padx=20)

value_1_var = tk.StringVar()
value_1 = tk.Entry(box_frame, width=23, textvariable=value_1_var)
value_1.focus()
value_1.pack(side='left', padx=20, pady=10)

to_label = tk.Label(box_frame, text="->", bg="#dfe6e9")
to_label.pack(side='left', pady=10)

value_2_var = tk.StringVar()
value_2 = tk.Entry(box_frame, width=23, textvariable=value_2_var)
value_2.pack(side='left', padx=20, pady=10)

# ______________________________________ Values Boxes Frame_________________________________________________

button_frame = tk.LabelFrame(window, background="#dfe6e9", border=0, relief=SUNKEN)
button_frame.pack(padx=20)

convert_button = tk.Button(button_frame, bg="#b2bec3", text='Convert', border=1, relief=SUNKEN, width=20,
                           font=("Arial", 11, 'bold'), command=action)
convert_button.pack(side='left', pady=10)

# ______________________________________ Formula Frame_________________________________________________

formula_frame = tk.LabelFrame(window, background="#dfe6e9", border=0, relief=SUNKEN)
formula_frame.pack(padx=20)

formula_answer_var = tk.StringVar()
formula_answer_label = tk.Label(formula_frame, textvariable=formula_answer_var, background="#dfe6e9", anchor='nw')
formula_answer_label.pack()

window.mainloop()
