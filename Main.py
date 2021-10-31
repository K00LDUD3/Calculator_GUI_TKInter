def EvalExp(exp):
    try:
        exp = exp.replace('^','**')
        return float(eval(exp))
    except ZeroDivisionError:
        return 'ERROR'



'''
a = 4
b = 3
c= a/b
d = float("{:.3f}".format(c))
print(d, type(d))
'''