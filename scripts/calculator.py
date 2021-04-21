import tkinter

root = tkinter.Tk()
root.title('Calculator')

label_display = tkinter.Label(root, text="Welcome")
label_display.grid(row=0, column=0, columnspan=4)




root.mainloop()