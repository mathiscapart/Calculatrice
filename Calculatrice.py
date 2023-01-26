import tkinter as tk

root = tk.Tk()

root.geometry("510x340")
root.title('Calculatrice')
root.resizable(False,False)
var_string = tk.StringVar(root)

def clear():
    var_string.set('')

def affichage(text):
    global btn_point
    var_string.set(var_string.get()+str(text))
    if '.' in var_string.get():
        btn_point.config(state=tk.DISABLED)

def additionner():
    global memoir
    global select_operation
    memoir = float(var_string.get())
    var_string.set("")
    btn_point.config(state=tk.NORMAL)
    select_operation = 1

def soustraction():
    global memoir
    global select_operation
    memoir = float(var_string.get())
    var_string.set("")
    btn_point.config(state=tk.NORMAL)
    select_operation = 2

def division():
    global memoir
    global select_operation
    memoir = float(var_string.get())
    var_string.set("")
    btn_point.config(state=tk.NORMAL)
    select_operation = 3

def multiplication():
    global memoir
    global select_operation
    memoir = float(var_string.get())
    var_string.set("")
    btn_point.config(state=tk.NORMAL)
    select_operation = 4


def result():
    if select_operation == 1:
        var_string.set(str(memoir + float(var_string.get())))
    if select_operation == 2:
        var_string.set(str(memoir - float(var_string.get())))
    if select_operation == 3:
        if float(var_string.get()) == 0:
            var_string.set('ERROR')
        var_string.set(str(memoir / float(var_string.get())))
    if select_operation == 4:
        var_string.set(str(memoir * float(var_string.get())))
    btn_point.config(state=tk.NORMAL)


btn_point = tk.Button(root, text=".", bg="#E6E6FA", padx=40, pady=20, font="Courier", state=tk.ACTIVE, command=lambda:affichage('.'))
btn0 = tk.Button(root, text="0", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(0)).grid(row=5, column=1)
btn_egal = tk.Button(root, text="=", bg="#a6a6ed", padx=145, pady=20, font="Courier", command= result).grid(row=5, column=2, columnspan=3)
btn1 = tk.Button(root, text="1", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(1)).grid(row= 4, column=0)
btn2 = tk.Button(root, text="2", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(2)).grid(row=4, column=1)
btn3 = tk.Button(root, text="3", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(3)).grid(row=4, column=2)
btn_moins = tk.Button(root, text="-", bg="#a6a6ed", padx=40, pady=20, font="Courier", command= soustraction).grid(row=4, column=3)
btn_multiplication = tk.Button(root, text="*", bg="#a6a6ed", padx=40, pady=20, font="Courier", command= multiplication).grid(row=4, column=4)
btn4 = tk.Button(root, text="4", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(4)).grid(row=3, column=0)
btn5 = tk.Button(root, text="5", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(5)).grid(row=3, column=1)
btn6 = tk.Button(root, text="6", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(6)).grid(row=3, column=2)
btn_plus = tk.Button(root, text="+", bg="#a6a6ed", padx=40, pady=20, font="Courier", command= additionner).grid(row=3, column=3)
btn_division = tk.Button(root, text="/", bg="#a6a6ed", padx=40, pady=20, font="Courier", command= division).grid(row=3, column=4)
btn7 = tk.Button(root, text="7", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(7)).grid(row=2, column=0)
btn8 = tk.Button(root, text="8", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(8)).grid(row=2, column=1)
btn9 = tk.Button(root, text="9", bg="#E6E6FA", padx=40, pady=20, font="Courier", command= lambda:affichage(9)).grid(row=2, column=2)
btn_reset = tk.Button(root, text="C", bg="#fae6e6",padx=90, pady=20, font="Courier", command= clear).grid(row=2, column=3, columnspan=2)
label = tk.Entry(bg='black', fg='white', borderwidth=3, relief="raised", font="Courier 24", textvariable= var_string).grid(row=0,column=0, columnspan=5, pady=10, padx=10)


btn_point.grid(row=5, column=0)
root.mainloop()