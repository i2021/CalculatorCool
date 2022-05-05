import math
import tkinter.messagebox
from tkinter import *

import sympy

root = Tk()
# Calculator dimensions
root.geometry("650x400+300+300")
# Attaching icon because why not :D
root.iconbitmap(True, "icon.ico")
# Gotta come up with a better name bruv
root.title("Scientific Calculator")

# Initializing the radians - degrees switch
switch = None


def btn1_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '1')


def btn2_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '2')


def btn3_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '3')


def btn4_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '4')


def btn5_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '5')


def btn6_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '6')


def btn7_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '7')


def btn8_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '8')


def btn9_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '9')


def btn0_clicked():
    if disp.get() == '0':
        disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def buttonplus_clicked():
    pos = len(disp.get())
    disp.insert(pos, '+')


def btnm_clicked():
    pos = len(disp.get())
    disp.insert(pos, '-')


def btnml_clicked():
    pos = len(disp.get())
    disp.insert(pos, '*')


def btnd_clicked():
    pos = len(disp.get())
    disp.insert(pos, '/')


def btnc_clicked(*args):
    disp.delete(0, END)
    disp.insert(0, '0')


def sin_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            ans = math.sin(math.radians(ans))
        else:
            ans = math.sin(ans)
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "sin error")


def cos_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            # Using degree setting
            ans = 1 - math.sin(math.radians(ans))
        else:
            # Using radians setting
            ans = math.cos(ans)
        # Displaying answer
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # Catching possible error
        tkinter.messagebox.showerror("Value Error", "cos error")


def tan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            # Using degree setting
            # Checking if number is a mod of 90 (undef)
            if abs(ans) % 90 == 0:
                # Checking if the num is zero
                if abs(ans) == 0:
                    # tan(0) = 0
                    disp.delete(0, END)
                    disp.insert(0, str(abs(ans)))
                else:
                    # Treating undef
                    disp.delete(0, END)
                    disp.insert(0, 'undef')
            else:
                # Calculating tan in degrees for non zeros or % 90s
                ans = math.tan(math.radians(ans))
        else:
            # Using radians setting
            ans = math.tan(ans)
        # Displaying the answer
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # Catching possible error
        tkinter.messagebox.showerror("Value Error", "tan error")


# arcsin action
def arcsin_clicked():
    try:
        # ans as float
        ans = float(disp.get())
        if switch is True:
            # degrees calculation
            ans = math.degrees(math.asin(ans))
        else:
            # radians calculation
            ans = math.asin(ans)
        # Push to display
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # catch exception
        tkinter.messagebox.showerror("Value Error", "arcsin error")


# arccos action
def arccos_clicked():
    try:
        # Grabbing as float
        ans = float(disp.get())
        if switch is True:
            # Degrees calculation
            ans = math.degrees(math.acos(ans))
        else:
            # Calculation in radians
            ans = math.acos(ans)
        # Push to display
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # Catch exceptions :S
        tkinter.messagebox.showerror("Value Error", "arccos error")


# arctangent action
def arctan_clicked():
    try:
        ans = float(disp.get())
        if switch is True:
            # Degrees
            ans = math.degrees(math.atan(ans))
        else:
            # Radians
            ans = math.atan(ans)
        # Display
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # Catch all the naughty
        tkinter.messagebox.showerror("Value Error", "actan error")


# Power of n
def pow_clicked():
    pos = len(disp.get())
    # Kinda user friendly
    disp.insert(pos, '**')


# Rounding the number action
def round_clicked():
    try:
        # Obtaining float
        ans = float(disp.get())
        # Rounding
        ans = round(ans)
        # Reset & display
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # Catch exceptions
        tkinter.messagebox.showerror("Value Error", "except on round")


# Logarithm action
def logarithm_clicked():
    try:
        ans = float(disp.get())
        # If log10(0) is used it needs to be undef
        if ans == 0:
            disp.delete(0, END)
            disp.insert(0, 'undef')
        else:
            # Using the log function
            ans = math.log10(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "except on logarithm")


# Factorial action
def fact_clicked():
    try:
        # Take factorial of number on display (non float)
        ans = math.factorial(int(disp.get()))
        disp.delete(0, END)
        disp.insert(0, str(ans))
    except Exception:
        # User did smth wrong. (Probably used a float as input)
        tkinter.messagebox.showerror("Value Error", "Maybe try doing non float factorial?")


# Square root action
def sqr_clicked():
    try:
        pos = len(disp.get())
        # User-friendly square root
        # x - value to root
        # n - power of root
        # don't forget to close the bracket after
        disp.insert(pos, '(x**(1/n)')
    except Exception:
        # Catching exception
        tkinter.messagebox.showerror("Value Error", "except on sqr")


# dot action
def dot_clicked():
    pos = len(disp.get())
    disp.insert(pos, '.')


# pi action
def pi_clicked():
    pos = len(disp.get())
    disp.insert(pos, 'pi')


# e- Mathematical constant
def e_clicked():
    pos = len(disp.get())
    disp.insert(pos, 'e')


# Opened bracket
def bl_clicked():
    pos = len(disp.get())
    disp.insert(pos, '(')


# Closed bracket
def br_clicked():
    pos = len(disp.get())
    disp.insert(pos, ')')


# Backspace action
def del_clicked():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos - 1])


# Radians - Degree switcher
def conv_clicked():
    global switch
    if switch is None:
        # Degrees for true
        switch = True
        conv_btn['text'] = "Deg"
    else:
        # Radians for false
        # Default
        switch = None
        conv_btn['text'] = "Rad"

# Natural log function
def ln_clicked():
    try:
        ans = float(disp.get())
        # If ln(0) is used it needs to be undef
        if ans == 0:
            # Stetting 'ans' as undef and displaying
            disp.delete(0, END)
            disp.insert(0, 'undef')
        else:
            # Normal natural log calculation using math library
            ans = math.log(ans)
            disp.delete(0, END)
            disp.insert(0, str(ans))
    except Exception:
        # Catching exception just in case
        tkinter.messagebox.showerror("Value Error", "except on ln")


def mod_clicked():
    pos = len(disp.get())
    disp.insert(pos, '%')


# Equals action
def btneq_clicked(*args):
    try:
        ans = disp.get()

        # If someone put in a coma instead of a dot, replace the comma w dot & slap them
        if "," in ans:
            ans = ans.replace(',', '.')

        # no nth root stated, using default (2) square root
        while "**(1/n)" in ans:
            ans = ans.replace('**(1/n)', '**(1/2)')

        # adding support with bracket multiplication without multiplication sign
        while ")(" in ans:
            ans = ans.replace(')(', ')*(')
        i = 0
        while i <= 9:
            line = str(i) + "("
            line2 = ")" + str(i)
            while line in ans:
                ans = ans.replace(line, str(i) + '*(')
            while line2 in ans:
                ans = ans.replace(line2, ')*' + str(i))
            i = i + 1

        # replacing pi
        i = 0
        while i <= 9:
            piy = str(i) + "pi"
            piy2 = "pi" + str(i)
            while piy in ans:
                ans = ans.replace(piy, str(i) + '*' + str(math.pi))
            while piy2 in ans:
                ans = ans.replace(piy2, str(math.pi) + '*' + str(i))
            i = i + 1
        while "pi" in ans:
            ans = ans.replace("pi", str(math.pi))

        # replacing e
        i = 0
        while i <= 9:
            piy = str(i) + "e"
            piy2 = "e" + str(i)
            while piy in ans:
                ans = ans.replace(piy, str(i) + '*' + str(math.e))
            while piy2 in ans:
                ans = ans.replace(piy2, str(math.e) + '*' + str(i))
            i = i + 1
        while "e" in ans:
            ans = ans.replace("e", str(math.e))

        # result display
        print(ans + " final")
        ans = eval(ans)
        disp.delete(0, END)
        disp.insert(0, ans)

        # prime evaluator
        switcher = sympy.isprime(ans)
        if switcher == 1:
            tkinter.messagebox.showinfo("Prime evaluator", str(ans) + " IS prime")
        else:
            tkinter.messagebox.showinfo("Prime evaluator", str(ans) + " is NOT prime")
    except:
        # Catch error and display message
        tkinter.messagebox.showerror("Value Error", "EQ went wrong somewhere")


# Label
disp = Entry(root, font="Verdana 20", fg="white", bg="#000000", bd=0, justify=RIGHT, insertbackground="#ffffff",
             cursor="arrow")
disp.bind("<Return>", btneq_clicked)
disp.bind("<Escape>", btnc_clicked)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 Buttons
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=TRUE, fill=BOTH)

pi_button = Button(btnrow1, text="π", font="Segoe 18", relief=GROOVE, bd=0, command=pi_clicked, fg="white",
                   bg="#333333")
pi_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

factorial_button = Button(btnrow1, text=" x! ", font="Segoe 18", relief=GROOVE, bd=0, command=fact_clicked, fg="white",
                          bg="#333333")
factorial_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

sin_button = Button(btnrow1, text="sin", font="Segoe 18", relief=GROOVE, bd=0, command=sin_clicked, fg="white",
                    bg="#333333")
sin_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

cos_button = Button(btnrow1, text="cos", font="Segoe 18", relief=GROOVE, bd=0, command=cos_clicked, fg="white",
                    bg="#333333")
cos_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

tan_button = Button(btnrow1, text="tan", font="Segoe 18", relief=GROOVE, bd=0, command=tan_clicked, fg="white",
                    bg="#333333")
tan_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn1 = Button(btnrow1, text="1", font="Segoe 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn2 = Button(btnrow1, text="2", font="Segoe 23", relief=GROOVE, bd=0, command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn3 = Button(btnrow1, text="3", font="Segoe 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)

buttonplus = Button(btnrow1, text="+", font="Segoe 23", relief=GROOVE, bd=0, command=buttonplus_clicked, fg="white",
                    bg="#333333")
buttonplus.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 Buttons
row2 = Frame(root)
row2.pack(expand=TRUE, fill=BOTH)

e_btn = Button(row2, text="e", font="Segoe 18", relief=GROOVE, bd=0, command=e_clicked, fg="white", bg="#333333")
e_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sqr_btn = Button(row2, text=" √x ", font="Segoe 18", relief=GROOVE, bd=0, command=sqr_clicked, fg="white",
                 bg="#333333")
sqr_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

sinh_btn = Button(row2, text="sin−1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=arcsin_clicked, fg="white",
                  bg="#333333")
sinh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

cosh_btn = Button(row2, text="cos-1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=arccos_clicked, fg="white",
                  bg="#333333")
cosh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

tanh_btn = Button(row2, text="tan-1", font="Segoe 11 bold", relief=GROOVE, bd=0, command=arctan_clicked, fg="white",
                  bg="#333333")
tanh_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn4 = Button(row2, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn5 = Button(row2, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn6 = Button(row2, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnm = Button(row2, text="-", font="Segoe 23", relief=GROOVE, bd=0, command=btnm_clicked, fg="white", bg="#333333")
btnm.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 Buttons
btnrow3 = Frame(root)
btnrow3.pack(expand=TRUE, fill=BOTH)

conv_btn = Button(btnrow3, text="Rad", font="Segoe 12 bold", relief=GROOVE, bd=0, command=conv_clicked, fg="white",
                  bg="#333333")
conv_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

round_btn = Button(btnrow3, text="round", font="Segoe 10 bold", relief=GROOVE, bd=0, command=round_clicked, fg="white",
                   bg="#333333")
round_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

ln_btn = Button(btnrow3, text="ln", font="Segoe 18", relief=GROOVE, bd=0, command=ln_clicked, fg="white", bg="#333333")
ln_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

logarithm_btn = Button(btnrow3, text="log", font="Segoe 17", relief=GROOVE, bd=0, command=logarithm_clicked, fg="white",
                       bg="#333333")
logarithm_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

pow_btn = Button(btnrow3, text="x^y", font="Segoe 17", relief=GROOVE, bd=0, command=pow_clicked, fg="white",
                 bg="#333333")
pow_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn7 = Button(btnrow3, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn8 = Button(btnrow3, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn9 = Button(btnrow3, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnml = Button(btnrow3, text="*", font="Segoe 23", relief=GROOVE, bd=0, command=btnml_clicked, fg="white", bg="#333333")
btnml.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons
btnrow4 = Frame(root)
btnrow4.pack(expand=TRUE, fill=BOTH)

mod_btn = Button(btnrow4, text="%", font="Segoe 21", relief=GROOVE, bd=0, command=mod_clicked, fg="white", bg="#333333")
mod_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

bl_btn = Button(btnrow4, text=" ( ", font="Segoe 21", relief=GROOVE, bd=0, command=bl_clicked, fg="white", bg="#333333")
bl_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

br_btn = Button(btnrow4, text=" ) ", font="Segoe 21", relief=GROOVE, bd=0, command=br_clicked, fg="white", bg="#333333")
br_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

dot_btn = Button(btnrow4, text=" • ", font="Segoe 21", relief=GROOVE, bd=0, command=dot_clicked, fg="white",
                 bg="#333333")
dot_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnc = Button(btnrow4, text="C", font="Segoe 23", relief=GROOVE, bd=0, command=btnc_clicked, fg="white", bg="#333333")
btnc.pack(side=LEFT, expand=TRUE, fill=BOTH)

del_btn = Button(btnrow4, text="⌫", font="Segoe 20", relief=GROOVE, bd=0, command=del_clicked, fg="white", bg="#333333")
del_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

btn0 = Button(btnrow4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)

btneq = Button(btnrow4, text="=", font="Segoe 23", relief=GROOVE, bd=0, command=btneq_clicked, fg="white", bg="#333333")
btneq.pack(side=LEFT, expand=TRUE, fill=BOTH)

btnd = Button(btnrow4, text="/", font="Segoe 23", relief=GROOVE, bd=0, command=btnd_clicked, fg="white", bg="#333333")
btnd.pack(side=LEFT, expand=TRUE, fill=BOTH)

# The loop for calculator calculating calculations for me to calculate less
root.mainloop()
