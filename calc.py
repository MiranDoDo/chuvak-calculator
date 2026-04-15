# Импорты

from tkinter import *

# Окно

window = Tk()
window.title("Chuvak Calculator")
window.geometry("340x240")
background_chuvak = PhotoImage(file = "./assets/backgrounds/chuvak.png")
window.iconphoto(False, background_chuvak)
window.maxsize(340, 240)
window.minsize(340, 240)

# Переменные

answer = ""
factorial = ""
actions = ['+', '-', '*', '/']


class Calculator_Actions():
    
    def __init__(self):
        pass

    def press(self):
        global answer
        answer += str(self)
        entry.set(answer)

    def actions(self):
        global answer
        if answer != "":
            result = str(eval(answer))
            entry.set(result)
            answer = ""
    
    def delete_everything(self):
        global answer
        entry.set("")
        answer = ""
    
    def factorial(self):
        global answer
        # Проверка
        if answer != "":
            if str(answer).rfind("+") > 0 or str(answer).rfind("*") > 0 or str(answer).rfind("/") > 0:
                pass
            # В будущем будет факториал с негативными числами
            elif answer.rfind("-") > 0:
                pass
            else:
                answer = int(answer)
                loop_int = int(answer)
                for k in range(1, loop_int):
                    answer *= k
        entry.set(answer)
        answer = ""

calculator = Calculator_Actions()


## UI

# Задний фон

label_background = Label(window, image=background_chuvak)
label_background.place(x=-110, y=-80, relwidth=2, relheight=2)

# Окошечко чисел

entry = StringVar()
entrywin = Entry(window, textvariable=entry)
entrywin.grid(columnspan=4, ipadx=70)

# Кнопки цифр

btn1 = Button(window, text='1',command=lambda: Calculator_Actions.press(1), height=1, width=7)
btn1.grid(row=3, column=0)

btn2 = Button(window, text='2',command=lambda: Calculator_Actions.press(2), height=1, width=7)
btn2.grid(row=3, column=1)


btn3 = Button(window, text='3',command=lambda: Calculator_Actions.press(3), height=1, width=7)
btn3.grid(row=3, column=2)


btn4 = Button(window, text='4',command=lambda: Calculator_Actions.press(4), height=1, width=7)
btn4.grid(row=4, column=0)


btn5 = Button(window, text='5',command=lambda: Calculator_Actions.press(5), height=1, width=7)
btn5.grid(row=4, column=1)


btn6 = Button(window, text='6',command=lambda: Calculator_Actions.press(6), height=1, width=7)
btn6.grid(row=4, column=2)


btn7 = Button(window, text='7',command=lambda: Calculator_Actions.press(7), height=1, width=7)
btn7.grid(row=5, column=0)


btn8 = Button(window, text='8',command=lambda: Calculator_Actions.press(8), height=1, width=7)
btn8.grid(row=5, column=1)


btn9 = Button(window, text='9',command=lambda: Calculator_Actions.press(9), height=1, width=7)
btn9.grid(row=5, column=2)


btn0 = Button(window, text='0',command=lambda: Calculator_Actions.press(0), height=1, width=7)
btn0.grid(row=6, column=0)

# Кнопки действий

plus = Button(window, text='+', command=lambda: Calculator_Actions.press('+'), height=1, width=8)
plus.grid(row=3, column=3)

minus = Button(window, text='-', command=lambda: Calculator_Actions.press('-'), height=1, width=8)
minus.grid(row=4, column=3)

mult = Button(window, text='*', command=lambda: Calculator_Actions.press('*'), height=1, width=8)
mult.grid(row=5, column=3)

div = Button(window, text='/', command=lambda: Calculator_Actions.press('/'), height=1, width=8)
div.grid(row=6, column=3)

fac = Button(window, text="fac", command=calculator.factorial, height=1, width=8)
fac.grid(row=7, column=3)

answ = Button(window, text="=", command=calculator.actions, height=1, width=7)
answ.grid(row=6, column=1)

delete = Button(window, text="del", command=calculator.delete_everything, height=1, width=7)
delete.grid(row=6, column=2)


window.mainloop()