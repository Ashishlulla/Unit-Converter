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
    if unit1 == 'centimeter':
        if unit2 == 'millimeter':
            a = str(int(value1)*10)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 10")
        elif unit2 == 'meter':
            a = str(int(value1)/100)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 100")
        elif unit2 == 'micrometer':
            a = str(int(value1)*10000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 10000")
        elif unit2 == 'nanometer':
            a = str(int(value1)*10000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 10000000")
        elif unit2 == 'kilometer':
            a = str(int(value1)*0.00001)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 100000")
        elif unit2 == 'mile':
            a = str(int(value1)/160934)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 160934")
        elif unit2 == 'feet':
            a = str(int(value1)/30.48)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 30.48")
        elif unit2 == 'inch':
            a = str(int(value1)/2.54)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 2.54")
    if unit1 == 'meter':
        if unit2 == 'centimeter':
                a = str(int(value1)*100)
                value_2_var.set(a)
                formula_answer_var.set("Formula:- Multilply length by 100")
        elif unit2 == 'millimeter':
                a = str(int(value1)*1000)
                value_2_var.set(a)
                formula_answer_var.set("Formula:- Multiply length by 1000")
        elif unit2 == 'micrometer':
                a = str(int(value1)*1000000)
                value_2_var.set(a)
                formula_answer_var.set("Formula:- Multiply length by 1000000")
        elif unit2 == 'nanometer':
                a = str(int(value1)*1000000000)
                value_2_var.set(a)
                formula_answer_var.set("Formula:- Multiply length by 1000000000")
        elif unit2 == 'kilometer':
            a = str(int(value1)*0.001)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 1000")
        elif unit2 == 'mile':
            a = str(int(value1)/1609)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 1609")
        elif unit2 == 'feet':
            a = str(int(value1)*3.281)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n Multiply the length value by 305")
        elif unit2 == 'inch':
            a = str(int(value1)/39.97)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- multiply the length by 39,37")
    if unit1 == 'micrometer':
        if unit2 == 'millimeter':
            a = str(int(value1)/1000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Divide length by 1000")
        elif unit2 == 'meter':
            a = str(int(value1)/1000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 1000000")
        elif unit2 == 'centimeter':
            a = str(int(value1)/10000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Divide length by 10000")
        elif unit2 == 'nanometer':
            a = str(int(value1)*1000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000")
        elif unit2 == 'kilometer':
            a = str(int(value1)/1000000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 1000000000")
        elif unit2 == 'mile':
            a = str(int(value1)/1609000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 1.609e+9")
        elif unit2 == 'feet':
            a = str(int(value1)/304800)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 304800")
        elif unit2 == 'inch':
            a = str(int(value1)/25400)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 25400")
    if unit1 == 'kilometer':
        if unit2 == 'centimeter':
            a = str(int(value1)*100000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 100000")
        elif unit2 == 'meter':
            a = str(int(value1)*1000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000")
        elif unit2 == 'micrometer':
            a = str(int(value1)*1000000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000000000")
        elif unit2 == 'nanometer':
            a = str(int(value1)*1000000000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 1000000000000")
        elif unit2 == 'millimeter':
            a = str(int(value1)*100000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- multiply length by 1000000")
        elif unit2 == 'mile':
            a = str(int(value1)/1.609)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 1.609")
        elif unit2 == 'feet':
            a = str(int(value1)*3281)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n multiply the length value by 3281")
        elif unit2 == 'inch':
            a = str(int(value1)*39370)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- multiply length by 39370")
    if unit1 == 'mile':
        if unit2 == 'millimeter':
            a = str(int(value1)*1609000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:-  multiply the length value by 1609000")
        elif unit2 == 'meter':
            a = str(int(value1)*1609)
            value_2_var.set(a)
            formula_answer_var.set("Formula:-  multiply the length value by 1609")
        elif unit2 == 'micrometer':
            a = str(int(value1)*1609000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:-  multiply the length value by 1609000000")
        elif unit2 == 'nanometer':
            a = str(int(value1)*1609000000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- , multiply the length value by 1609000000000")
        elif unit2 == 'kilometer':
            a = str(int(value1)*1.609)
            value_2_var.set(a)
            formula_answer_var.set("Formula:-  multiply the length value by 1.609")
        elif unit2 == 'centimeter':
            a = str(int(value1)*160934)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n multiply the length value by 160934")
        elif unit2 == 'feet':
            a = str(int(value1)*5280)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply the length value by 5280")
        elif unit2 == 'inch':
            a = str(int(value1)*63360)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 63360")
    if unit1 == 'feet':
        if unit2 == 'centimeter':
            a = str(int(value1)*30.48)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 30.48")
        elif unit2 == 'millimeter':
            a = str(int(value1)*304.8)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result, "
                                   "\nmultiply the length value by 305")
        elif unit2 == 'micrometer':
            a = str(int(value1)* 304800)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 304800")
        elif unit2 == 'nanometer':
            a = str(int(value1)*304800000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 304800000")
        elif unit2 == 'kilometer':
            a = str(int(value1)/3281)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result, \ndivide the length value by 3281")
        elif unit2 == 'mile':
            a = str(int(value1)/5281)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide the length value by 5281")
        elif unit2 == 'meter':
            a = str(int(value1)/3.281)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result,\n divide the length value by 305")
        elif unit2 == 'inch':
            a = str(int(value1)*12)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- multiply the length by 12")
    if unit1 == 'inch':
        if unit2 == 'millimeter':
            a = str(int(value1)*25.4)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 25.4")
        elif unit2 == 'meter':
            a = str(int(value1)/39.37)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide length by 39.37")
        elif unit2 == 'centimeter':
            a = str(int(value1)/2.54)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 2.54")
        elif unit2 == 'nanometer':
            a = str(int(value1)*2.5400000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- Multiply length by 2.5400000")
        elif unit2 == 'kilometer':
            a = str(int(value1)/39370)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- for an approximate result, \ndivide the length value by 39370")
        elif unit2 == 'mile':
            a = str(int(value1)/1609000000)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- divide the length value by  63360")
        elif unit2 == 'feet':
            a = str(int(value1)/12)
            value_2_var.set(a)
            formula_answer_var.set("Formula:-divide the length value by 12")
        elif unit2 == 'micrometer':
            a = str(int(value1)*25400)
            value_2_var.set(a)
            formula_answer_var.set("Formula:- multiply length by 25400")
        

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
