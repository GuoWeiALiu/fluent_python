import io
import numbers
import tkinter

print(bool.__mro__)
def print_mro(cls):
    print(','.join(c.__name__ for c in cls.__mro__))

print_mro(bool)
print_mro(numbers.Integral)
print_mro(io.TextIOWrapper)
print_mro(tkinter.Text)
print_mro(tkinter.Toplevel)
print_mro(tkinter.Widget)
print_mro(tkinter.Button)
print_mro(tkinter.Entry)
