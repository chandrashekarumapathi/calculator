import tkinter
from loguru import logger


class CalculatorLayout:
    def __init__(self):
        self.expression = ""
        self.root = tkinter.Tk()
        self.root.title('Calculator')
        self.create_label()
        self.create_buttons()
        self.root.mainloop()

    def add_button(self, value):
        label_display = self.create_label()
        self.expression += value
        label_display.config(text=self.expression)
        # print(self.expression)
        return self.expression

    def calculate(self):
        label_display = self.create_label()

        result = eval(self.expression)
        label_display.config(text=result)
        self.expression = str(result)

    def clear(self):
        label_display = self.create_label()
        self.expression = ""
        label_display.config(text=self.expression)

    def create_label(self):
        label_display = tkinter.Label(self.root, text="")
        label_display.grid(row=0, column=0, columnspan=4)
        return label_display

    def create_buttons(self):
        button_9 = tkinter.Button(self.root, text='9', command=lambda: self.add_button('9'))
        button_9.grid(row=1, column=0)

        button_8 = tkinter.Button(self.root, text='8', command=lambda: self.add_button('8'))
        button_8.grid(row=1, column=1)

        button_7 = tkinter.Button(self.root, text='7', command=lambda: self.add_button('7'))
        button_7.grid(row=1, column=2)

        button_add = tkinter.Button(self.root, text='+', command=lambda: self.add_button('+'))
        button_add.grid(row=1, column=3)

        button_6 = tkinter.Button(self.root, text='6', command=lambda: self.add_button('6'))
        button_6.grid(row=2, column=0)

        button_5 = tkinter.Button(self.root, text='5', command=lambda: self.add_button('5'))
        button_5.grid(row=2, column=1)

        button_4 = tkinter.Button(self.root, text='4', command=lambda: self.add_button('4'))
        button_4.grid(row=2, column=2)

        button_sub = tkinter.Button(self.root, text='-', command=lambda: self.add_button('-'))
        button_sub.grid(row=2, column=3)

        button_3 = tkinter.Button(self.root, text='3', command=lambda: self.add_button('3'))
        button_3.grid(row=3, column=0)

        button_2 = tkinter.Button(self.root, text='2', command=lambda: self.add_button('2'))
        button_2.grid(row=3, column=1)

        button_1 = tkinter.Button(self.root, text='1', command=lambda: self.add_button('1'))
        button_1.grid(row=3, column=2)

        button_mul = tkinter.Button(self.root, text='*', command=lambda: self.add_button('*'))
        button_mul.grid(row=3, column=3)

        button_dot = tkinter.Button(self.root, text='.', command=lambda: self.add_button('.'))
        button_dot.grid(row=4, column=0)

        button_0 = tkinter.Button(self.root, text='0', command=lambda: self.add_button('0'))
        button_0.grid(row=4, column=1)

        button_eq = tkinter.Button(self.root, text='=', command=lambda: self.calculate())
        button_eq.grid(row=4, column=2)

        button_div = tkinter.Button(self.root, text='/', command=lambda: self.add_button('/'))
        button_div.grid(row=4, column=3)

        button_clear = tkinter.Button(self.root, text='Clear', command=lambda: self.clear())
        button_clear.grid(row=5, column=0, columnspan=4)


test = CalculatorLayout()