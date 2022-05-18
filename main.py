import math
import tkinter.messagebox
from tkinter import *

root = Tk()
# Calculator dimensions
root.geometry("300x500+300+300")
# Gotta come up with a better name bruv
root.title("Scientific Calculator")

# Initializing the radians - degrees switch
switch = None


def clicked_1():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '1')


def clicked_2():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '2')


def clicked_3():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '3')


def clicked_4():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '4')


def clicked_5():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '5')


def clicked_6():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '6')


def clicked_7():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '7')


def clicked_8():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '8')


def clicked_9():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '9')


def clicked_0():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '0')


def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)


def plus():
    pos = len(disp.get())
    disp.insert(pos, '+')


# Nothing function
def nothing(*args):
    return


# Dot function
def dot():
    pos = len(disp.get())
    disp.insert(pos, '.')


def minus():
    key_event()
    pos = len(disp.get())
    disp.insert(pos, '-')


def multiply():
    pos = len(disp.get())
    disp.insert(pos, '*')


def divide():
    pos = len(disp.get())
    disp.insert(pos, '/')


def c(*args):
    disp.delete(0, END)
    pos = len(disp.get())
    disp.insert(pos, '0')


def prime():
    try:
        ans = float(disp.get())
        num = int(ans)
        # Doing this avoids 3.0 throwing an error despite being prime
        # If given number is greater than 1
        if ans == num and num > 1:
            # Iterate from 2 to n / 2
            for i in range(2, int(num / 2) + 1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    tkinter.messagebox.showinfo("Prime evaluator", "Number is NOT prime")
                    break
            else:
                tkinter.messagebox.showinfo("Prime evaluator", "Number IS prime")
        else:
            # Negative numbers are not prime
            # Decimals are not prime unless they are == int
            tkinter.messagebox.showinfo("Prime evaluator", "Number is NOT prime")
    except Exception:
        # Catching errors & displaying message
        tkinter.messagebox.showerror("Value Error", "Prime Error")


def scientific():
    try:
        # scientific notation converter
        # .2 stands for "print a float with 2 decimal places", so %.4 would print 33.3333
        # we attach E at the end
        ans = "{:.2E}".format(float(disp.get()))
        update_display(ans)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Scientific conversion Error")


def update_display(ans):
    # Clear display
    disp.delete(0, END)
    # Insert answer
    disp.insert(0, ans)


def percentage():
    try:
        # percentage converter
        ans = float(disp.get())
        # .2 stands for "print a float with 2 decimal places", so %.4f would print 33.3333
        ans = "{:.2%}".format(ans)
        update_display(str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Percentage Error")


def sin():
    try:
        ans = float(disp.get())
        if switch is True:
            # Using degree setting
            ans = math.sin(math.radians(ans))
        else:
            # Using radians
            ans = math.sin(ans)
        update_display(str(ans))
    except Exception:
        # Catching exception on sin
        tkinter.messagebox.showerror("Value Error", "Sin Error")


def cos():
    try:
        ans = float(disp.get())
        if switch is True:
            # Using degree setting
            ans = 1 - math.sin(math.radians(ans))
        else:
            # Using radians setting
            ans = round(math.cos(ans), 5)
        # Displaying answer
        update_display(str(ans))
    except Exception:
        # Catching possible error
        tkinter.messagebox.showerror("Value Error", "Cos Error")


def tan():
    try:
        ans = float(disp.get())
        if switch is True:
            # Using degree setting
            # Checking if number is a mod of 90 (undef)
            if abs(ans) % 90 == 0:
                # Checking if the num is zero
                if abs(ans) == 0:
                    # tan(0) = 0
                    update_display(str(abs(ans)))
                    return
                else:
                    # Treating undef
                    ans = 'undef'
            else:
                # Calculating tan in degrees for non zeros or % 90s
                ans = math.tan(math.radians(ans))
        else:
            # Using radians setting
            ans = math.tan(ans)
        # Displaying the answer
        update_display(str(ans))
    except Exception:
        # Catching possible error
        tkinter.messagebox.showerror("Value Error", "tan error")


# arcsin action
def arcsin():
    try:
        # ans as float
        ans = float(disp.get())
        if switch is True:
            # Degrees calculation
            if ans > 1 or ans < -1:
                # In degrees arc sin should give undef when below -1 or above 1
                ans = 'undef'
            else:
                ans = math.degrees(math.asin(ans))
        else:
            # Calculation in radians
            if ans > 1 or ans < -1:
                # In radians arc sin should give non-real output when below -1 or above 1
                tkinter.messagebox.showwarning("Info", "Non-real result")
            else:
                ans = math.asin(ans)
        # Push to display
        update_display(str(ans))
    except Exception:
        # catch exception
        tkinter.messagebox.showerror("Value Error", "Arcsine Error")


# arccos action
def arccos():
    try:
        # Grabbing as float
        ans = float(disp.get())
        if switch is True:
            # Degrees calculation
            if ans > 1 or ans < -1:
                # In degrees arc cos should give undef when below -1 or above 1
                ans = 'undef'
            else:
                ans = math.degrees(math.acos(ans))

        else:
            # Calculation in radians
            if ans > 1 or ans < -1:
                # In radians arc cos should give non-real output when below -1 or above 1
                tkinter.messagebox.showwarning("Info", "Non-real result")
            else:
                ans = round(math.acos(ans), 5)
        # Push to display
        update_display(str(ans))
    except Exception:
        # Catch exceptions :S
        tkinter.messagebox.showerror("Value Error", "Arcosine Error")


# arctangent action
def arctan():
    try:
        ans = float(disp.get())
        if switch is True:
            # Degrees
            ans = math.degrees(math.atan(ans))
        else:
            # Radians
            ans = math.atan(ans)
        # Display
        update_display(str(ans))
    except Exception:
        # Catch all the naughty
        tkinter.messagebox.showerror("Value Error", "Arctan Error")


# Power of n
def power():
    pos = len(disp.get())
    # Kinda user friendly
    disp.insert(pos, '^')


# Logarithm action
def logarithm():
    try:
        ans = float(disp.get())
        # If log10(0) is used it needs to be undef
        if ans == 0:
            ans = 'undef'
        else:
            # Using the log function
            ans = math.log10(ans)
        update_display(str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Logarithm Error")


# Factorial action
def factorial():
    try:
        # Take factorial of number on display (non float)
        ans = math.factorial(int(disp.get()))
        update_display(str(ans))
    except Exception:
        # User did smth wrong. (Probably used a float as input)
        tkinter.messagebox.showerror("Value Error", "Maybe try doing non float factorial?")


# Absolute action
def absolute():
    try:
        # Take absolute of number on display
        ans = abs(float(disp.get()))
        update_display(str(ans))
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Absolute Eoor")


# 10^x action
def p_10x():
    try:
        pos = len(disp.get())
        disp.insert(pos, '*(10^')
    except Exception:
        # Catching exception
        tkinter.messagebox.showerror("Value Error", "p_10x Error")


# Square root action
def root_c():
    try:
        pos = len(disp.get())
        # User-friendly square root
        # x - value to root
        # n - power of root
        # don't forget to close the bracket after
        if str(disp.get()) == '0':
            disp.delete(0, END)
        disp.insert(pos, '(x^(1/n)')
    except Exception:
        # Catching exception
        tkinter.messagebox.showerror("Value Error", "Root function error")


# pi action
def pi():
    pos = len(disp.get())
    if str(disp.get()) == '0':
        disp.delete(0, END)
        disp.insert(pos, 'pi')
    else:
        disp.insert(pos, 'pi')


# e- Mathematical constant
def e():
    pos = len(disp.get())
    if str(disp.get()) == '0':
        disp.delete(0, END)
        disp.insert(pos, 'e')
    else:
        disp.insert(pos, 'e')


# Opened bracket
def bopen():
    pos = len(disp.get())
    disp.insert(pos, '(')


# Closed bracket
def bclosed():
    pos = len(disp.get())
    disp.insert(pos, ')')


# Backspace action
def backspace():
    # Getting cursor position on screen
    pos = len(disp.get())
    # Getting the whole function from display
    display = str(disp.get())
    # If function is empty we replace it with 0
    if display == '':
        disp.insert(0, '0')
    # If function is a space we replace it with 0 also
    elif display == ' ':
        disp.insert(0, '0')
    # If function is only 0 we do nothing
    elif display == '0':
        pass
    else:
        # Otherwise, we delete everything
        disp.delete(0, END)
        # Insert answer without the last character
        disp.insert(0, display[0:pos - 1])


# Radians - Degree switcher
def converter():
    global switch
    if switch is None:
        # Degrees for true
        switch = True
        converter_button['text'] = "DEG"
    else:
        # Radians for false
        # Default
        switch = None
        converter_button['text'] = "RAD"


# Natural log function
def ln():
    try:
        ans = float(disp.get())
        # If ln(0) is used it needs to be undef
        if ans == 0:
            # Stetting 'ans' as undef
            ans = 'undef'
        else:
            # Normal natural log calculation using math library
            ans = math.log(ans)
        # Displaying undef or answer
        update_display(str(ans))
    except Exception:
        # Catching exception just in case
        tkinter.messagebox.showerror("Value Error", "Natural logarithm Error")


def modulo():
    pos = len(disp.get())
    disp.insert(pos, '%')


def replacement(ans):
    # If someone put in a coma instead of a dot, replace the comma w dot & slap them
    if ',' in ans:
        ans = ans.replace(',', '.')

    # no nth root stated, using default (2) square root
    while '^(1/n)' in ans:
        ans = ans.replace('^(1/n)', '^(1/2)')

    # Replace the '^' symbol with power
    while '^' in ans:
        ans = ans.replace('^', '**')

    # adding support with bracket multiplication without multiplication sign
    while ')(' in ans:
        # If closing and opening brackets are next to each other we assume there has to be a multiplication sign
        # inbetween them
        ans = ans.replace(')(', ')*(')
    # replacing pi
    i = 0
    # From 0 --> 9
    while i <= 9:
        piy = str(i) + 'pi'
        piy2 = 'pi' + str(i)
        # Adding multiplication sign
        line = str(i) + '('
        line2 = ')' + str(i)
        while piy in ans:
            # If there is a number next to pi on left side & no multiplication sign, we put it there
            ans = ans.replace(piy, str(i) + '*' + str(math.pi))
        while piy2 in ans:
            # If there is a number next to pi on right side & no multiplication sign, we put it there
            ans = ans.replace(piy2, str(math.pi) + '*' + str(i))
        while line in ans:
            # If there is a number next to opening bracket & no multiplication sign, we put it there
            ans = ans.replace(line, str(i) + '*(')
        while line2 in ans:
            # If there is a number next to closing bracket & no multiplication sign, we put it there
            ans = ans.replace(line2, ')*' + str(i))
        i = i + 1
    while 'pipi' in ans:
        # We need to support pipi and other iterations because I deiced so
        ans = ans.replace('pipi', 'pi*pi')
    while 'pi' in ans:
        # Replacing pi from string to a constant math.pi
        ans = ans.replace('pi', str(math.pi))

    # replacing e
    i = 0
    # From 0--> 9
    while i <= 9:
        piy = str(i) + 'e'
        piy2 = 'e' + str(i)
        while piy in ans:
            # If there is a number next to e on left side & no multiplication sign, we put it there
            ans = ans.replace(piy, str(i) + '*' + str(math.e))
        while piy2 in ans:
            # If there is a number next to e on right side & no multiplication sign, we put it there
            ans = ans.replace(piy2, str(math.e) + '*' + str(i))
        i = i + 1
    while 'ee' in ans:
        # We need to support ee and other iterations because I deiced so
        ans = ans.replace('ee', 'e*e')
    while 'e' in ans:
        # Replacing e from string to a constant math.e
        ans = ans.replace('e', str(math.e))
    return ans


# Equals action
def equals(*args):
    try:
        # Replacement function
        ans = replacement(disp.get())

        # Evaluate the function after all the replacements have been made
        # !! Compromise !!
        # To avoid floating point caused offset we are rounding all the answers to 10 decimal places
        # Example without floating point offset fix (.1*.1 is 0.010000000000000002 not 0.01)
        ans = round(eval(ans), 5)
        update_display(str(ans))
        return float(ans)
    except:
        # Catch error and display message
        tkinter.messagebox.showerror("Value Error", "Maybe you should check the function for mistakes?")


# Label
disp = Entry(root, font="Verdana 20", fg="#ffffff", bg="#1a1919", bd=14, justify=RIGHT, insertbackground="#ffffff",
             cursor="arrow")
disp.bind("<Return>", equals)
disp.bind("<Escape>", c)
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
disp.bind("<Key-->", key_event)
disp.bind("<Key-.>", nothing)
disp.insert(0, '0')
disp.focus_set()
disp.pack(expand=TRUE, fill=BOTH)

# Row 1 buttons (RAD, sin, tan, cos, del)
row1 = Frame(root, bg="#3b3838")
row1.pack(expand=TRUE, fill=BOTH)

converter_button = Button(row1, text="RAD", font="Segoe 11", relief=GROOVE, bd=0, command=converter, fg="#ffffff",
                          bg="#0f0f0f")
sin_button = Button(row1, text="sin", font="Segoe 10", relief=GROOVE, bd=0, command=sin, fg="#ffffff", bg="#0f0f0f")
cos_button = Button(row1, text="cos", font="Segoe 10", relief=GROOVE, bd=0, command=cos, fg="#ffffff", bg="#0f0f0f")
tan_button = Button(row1, text="tan", font="Segoe 10", relief=GROOVE, bd=0, command=tan, fg="#ffffff", bg="#0f0f0f")
backspace_button = Button(row1, text="⌫", font="Segoe 15", relief=GROOVE, bd=0, command=backspace, fg="#ffffff",
                          bg="#0f0f0f")
converter_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
sin_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
cos_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
tan_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
backspace_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 2 buttons (%, arcsin, arccos, arctan, sci)
row2 = Frame(root)
row2.pack(expand=TRUE, fill=BOTH)

percentage_button = Button(row2, text=" %", font="Segoe 18", relief=GROOVE, bd=0, command=percentage, fg="#ffffff",
                           bg="#0f0f0f")
arcsin_button = Button(row2, text=" sin-1 ", font="Segoe 8", relief=GROOVE, bd=0, command=arcsin, fg="#ffffff",
                       bg="#0f0f0f")
arccos_button = Button(row2, text=" cos-1 ", font="Segoe 8", relief=GROOVE, bd=0, command=arccos, fg="#ffffff",
                       bg="#0f0f0f")
arctan_button = Button(row2, text=" tan-1 ", font="Segoe 8", relief=GROOVE, bd=0, command=arctan, fg="#ffffff",
                       bg="#0f0f0f")
scientific_button = Button(row2, text="sci  ", font="Segoe 11", relief=GROOVE, bd=0, command=scientific, fg="#ffffff",
                           bg="#0f0f0f")

percentage_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
arcsin_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
arccos_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
arctan_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
scientific_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 3 buttons (pi, e, abs(x), Np, mod)
row3 = Frame(root)
row3.pack(expand=TRUE, fill=BOTH)

pi_button = Button(row3, text="π", font="Segoe 21", relief=GROOVE, bd=0, command=pi, fg="#ffffff", bg="#0f0f0f")
e_button = Button(row3, text="e", font="Segoe 18", relief=GROOVE, bd=0, command=e, fg="#ffffff", bg="#0f0f0f")
absolute_button = Button(row3, text="| x |", font="Segoe 12", relief=GROOVE, bd=0, command=absolute, fg="#ffffff",
                         bg="#0f0f0f")
prime_button = Button(row3, text="Np", font="Segoe 11", relief=GROOVE, bd=0, command=prime, fg="#ffffff", bg="#0f0f0f")
modulo_button = Button(row3, text="mod", font="Segoe 11", relief=GROOVE, bd=0, command=modulo, fg="#ffffff",
                       bg="#0f0f0f")

pi_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
e_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
absolute_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
prime_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
modulo_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 4 Buttons ( n√x, (, ), n!, ÷)
row4 = Frame(root)
row4.pack(expand=TRUE, fill=BOTH)

root_button = Button(row4, text="n√x", font="Segoe 13", relief=GROOVE, bd=0, command=root_c, fg="#ffffff", bg="#0f0f0f")
bopen_button = Button(row4, text="(", font="Segoe 16", relief=GROOVE, bd=0, command=bopen, fg="#ffffff", bg="#0f0f0f")
bclosed_button = Button(row4, text=")", font="Segoe 16", relief=GROOVE, bd=0, command=bclosed, fg="#ffffff",
                        bg="#0f0f0f")
factorial_button = Button(row4, text="n!", font="Segoe 15", relief=GROOVE, bd=0, command=factorial, fg="#ffffff",
                          bg="#0f0f0f")
divide_button = Button(row4, text="÷", font="Segoe 18", relief=GROOVE, bd=0, command=divide, fg="#ffffff", bg="#0f0f0f")

root_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
bopen_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
bclosed_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
factorial_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
divide_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 5 Buttons ( xⁿ, 7, 8, 9, ×)
row5 = Frame(root)
row5.pack(expand=TRUE, fill=BOTH)

power_button = Button(row5, text="xⁿ", font="Segoe 19", relief=GROOVE, bd=0, command=power, fg="#ffffff", bg="#0f0f0f")
button_7 = Button(row5, text="7", font="Segoe 19", relief=GROOVE, bd=0, command=clicked_7, fg="#ffffff", bg="#0a0a0a")
button_8 = Button(row5, text="8", font="Segoe 18", relief=GROOVE, bd=0, command=clicked_8, fg="#ffffff", bg="#0a0a0a")
button_9 = Button(row5, text="9", font="Segoe 19", relief=GROOVE, bd=0, command=clicked_9, fg="#ffffff", bg="#0a0a0a")

multiply_button = Button(row5, text="×", font="Segoe 19", relief=GROOVE, bd=0, command=multiply, fg="#ffffff",
                         bg="#0f0f0f")

power_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_7.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_8.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_9.pack(side=LEFT, expand=TRUE, fill=BOTH)
multiply_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 6 Buttons ( 10^x, 4, 5, 6, −)
row6 = Frame(root)
row6.pack(expand=TRUE, fill=BOTH)

p_10x_button = Button(row6, text="10^x", font="Segoe 11", relief=GROOVE, bd=0, command=p_10x, fg="#ffffff",
                      bg="#0f0f0f")
button_4 = Button(row6, text="4", font="Segoe 19", relief=GROOVE, bd=0, command=clicked_4, fg="#ffffff", bg="#0a0a0a")
button_5 = Button(row6, text="5", font="Segoe 18", relief=GROOVE, bd=0, command=clicked_5, fg="#ffffff", bg="#0a0a0a")
button_6 = Button(row6, text="6", font="Segoe 17", relief=GROOVE, bd=0, command=clicked_6, fg="#ffffff", bg="#0a0a0a")
minus_button = Button(row6, text="-", font="Segoe 22", relief=GROOVE, bd=0, command=minus, fg="#ffffff", bg="#0f0f0f")

p_10x_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_4.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_5.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_6.pack(side=LEFT, expand=TRUE, fill=BOTH)
minus_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 7 Buttons (log(), 1, 2, 3, +)
row7 = Frame(root)
row7.pack(expand=TRUE, fill=BOTH)

logarithm_button = Button(row7, text="log", font="Segoe 14", relief=GROOVE, bd=0, command=logarithm, fg="#ffffff",
                          bg="#0f0f0f")
button_1 = Button(row7, text="1", font="Segoe 18", relief=GROOVE, bd=0, command=clicked_1, fg="#ffffff", bg="#0a0a0a")
button_2 = Button(row7, text="2", font="Segoe 19", relief=GROOVE, bd=0, command=clicked_2, fg="#ffffff", bg="#0a0a0a")
button_3 = Button(row7, text="3", font="Segoe 19", relief=GROOVE, bd=0, command=clicked_3, fg="#ffffff", bg="#0a0a0a")
plus_button = Button(row7, text="+", font="Segoe 19", relief=GROOVE, bd=0, command=plus, fg="#ffffff", bg="#0f0f0f")
logarithm_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_1.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_2.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_3.pack(side=LEFT, expand=TRUE, fill=BOTH)
plus_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Row 8 Buttons (ln(), •, 0, C, =)
row8 = Frame(root)
row8.pack(expand=TRUE, fill=BOTH)

ln_button = Button(row8, text="ln", font="Segoe 18", relief=GROOVE, bd=0, command=ln, fg="#ffffff", bg="#0f0f0f")
dot_button = Button(row8, text="•", font="Segoe 18", relief=GROOVE, bd=0, command=dot, fg="#ffffff", bg="#0a0a0a")
button_0 = Button(row8, text="0", font="Segoe 18", relief=GROOVE, bd=0, command=clicked_0, fg="#ffffff", bg="#0a0a0a")
c_button = Button(row8, text="C", font="Segoe 18", relief=GROOVE, bd=0, command=c, fg="#ffffff", bg="#0a0a0a")
equals_button = Button(row8, text="=", font="Segoe 18", relief=GROOVE, bd=2, command=equals, fg="#ffffff", bg="#7a470c")

ln_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
dot_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_0.pack(side=LEFT, expand=TRUE, fill=BOTH)
c_button.pack(side=LEFT, expand=TRUE, fill=BOTH)
equals_button.pack(side=LEFT, expand=TRUE, fill=BOTH)

# The loop for calculator calculating calculations for me to calculate less
root.mainloop()
