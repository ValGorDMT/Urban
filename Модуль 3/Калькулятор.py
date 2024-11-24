import tkinter as tk

window = tk.Tk()

window.title('Калькулятор')
window.geometry('170x400')
window.resizable(False, False)

number1 = tk.Label(window, text='Первое число:')
number1.place(x=20, y= 10)
number1_emtry = tk.Entry()
number1_emtry.place(x=20, y = 30)

number2 = tk.Label(window, text='Второе число:')
number2.place(x=20, y= 110)
number2_emtry = tk.Entry()
number2_emtry.place(x=20, y = 130)

button_add = tk.Button(window, text="+", width=2, height=2)
button_add.place(x=20, y=160)

button_add = tk.Button(window, text="-", width=2, height=2)
button_add.place(x=50, y=160)

button_add = tk.Button(window, text="*", width=2, height=2)
button_add.place(x=80, y=160)

button_add = tk.Button(window, text="/", width=2, height=2)
button_add.place(x=110, y=160)

answer = tk.Label(window, text='Ответ:')
answer.place(x=20, y= 310)
answer_emtry = tk.Entry()
answer_emtry.place(x=20, y = 330)




window.mainloop()