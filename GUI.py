from tkinter import *
from types import BuiltinMethodType

root = Tk()
root.title('Calculator')

button_list = []

#button Param Variables
button_width = 5
button_height = 5
button_padx = 0
button_pady = 10
button_borderwidth = 5

#func
def EvalExp():
    exp = label.cget('text')
    try:
        exp = exp.replace('^','**')
        label.config(text=str(float(eval(exp))))
    except:
        label.config(text='ERROR')



def clear():
    label.config(text='')

def AddNumOperator(OpNum):
    exp = label.cget('text')
    print(type(exp), exp)
    exp.replace('ERROR','')
    exp = exp+' '+OpNum
    print('exp after concatinating: ',exp)
    label.config(text=exp)

#Button customizer func
def createNumberButtons():
    #assigning values of buttons (1-9, 0)
    for i in range(0,9):
        button_list.append(Button(root, width=button_width, text = (i+1)))
        button_list[i].grid(row=i//3+1, column=i%3, padx = button_padx, pady = button_pady)

    button_list.append(Button(root, width=button_width, text = 0 ))
    button_list[9].grid(row=4, column=1, padx = button_padx, pady = button_pady)

    
    button_list[9].config(command = lambda: AddNumOperator('0'))

    button_list[0].config(command = lambda: AddNumOperator('1'))
    button_list[1].config(command = lambda: AddNumOperator('2'))
    button_list[2].config(command = lambda: AddNumOperator('3'))
    button_list[3].config(command = lambda: AddNumOperator('4'))
    button_list[4].config(command = lambda: AddNumOperator('5'))
    button_list[5].config(command = lambda: AddNumOperator('6'))
    button_list[6].config(command = lambda: AddNumOperator('7'))
    button_list[7].config(command = lambda: AddNumOperator('8'))
    button_list[8].config(command = lambda: AddNumOperator('9'))



#Clear button
AC = Button(root, width=button_width, text = 'Clear', command = clear)
AC.grid(row=1, column=4)

#operator buttons
op_add = Button(root, width=button_width, text='+', command=lambda: AddNumOperator('+'))
op_subtract = Button(root, width=button_width, text='-', command=lambda: AddNumOperator('-'))
op_multiply = Button(root, width=button_width, text='*', command=lambda: AddNumOperator('*'))
op_divide = Button(root, width=button_width, text='/', command=lambda: AddNumOperator('/'))
op_modulus = Button(root, width=button_width, text='mod', command=lambda: AddNumOperator('%'))

op_add.grid(row=1, column=3, padx = button_padx, pady = button_pady)
op_subtract.grid(row=2, column=3, padx = button_padx, pady = button_pady)
op_multiply.grid(row=3, column=3, padx = button_padx, pady = button_pady)
op_divide.grid(row=4, column=3, padx = button_padx, pady = button_pady)
op_modulus.grid(row=4, column=0, padx=button_padx, pady=button_pady)

#'=' button
__equal = Button(root, width=button_width, text='=', command=EvalExp)
__equal.grid(row=4, column=2, padx = button_padx, pady = button_pady)


#Creating Display Label
label = Label(root, text='', width=30, borderwidth=5)
label.grid(row=0, column=0, columnspan=4)
createNumberButtons()
root.mainloop()

