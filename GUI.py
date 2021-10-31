from tkinter import *
from types import BuiltinMethodType

root = Tk()
root.title('Calculator')

#Param Variables
button_width = 5
button_height = 5
button_padx = 0
button_pady = 10
button_borderwidth = 5

#Button customizer func
def createNumberButtons():
    #assigning values of buttons (1-9, 0)
    button_list = []
    for i in range(0,9):
        button_list.append(Button(root, width=button_width, text = (i+1), command = lambda: AddNumOperator(str(i+1))))
        button_list[i].grid(row=i//3+1, column=i%3, padx = button_padx, pady = button_pady)

    button_list.append(Button(root, width=button_width, text = 0, command = lambda: AddNumOperator(str(0))))
    button_list[9].grid(row=4, column=1, padx = button_padx, pady = button_pady)

def clear():
    label.config(text='')

def AddNumOperator(val):
    x = label.cget('text')
    x = x+val
    label.config(text=x)

#Clear button
AC = Button(root, width=button_width, text = 'Clear', command = clear)
AC.grid(row=4, column=0)
#Creating Display Label
label = Label(root, text='', width=25, borderwidth=5)
label.grid(row=0, column=0, columnspan=3)
createNumberButtons()
root.mainloop()