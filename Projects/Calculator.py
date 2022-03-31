'''
print("Hello")

a,b = input ("Enter two numbers : ").split(" ")

print ("What would you like to do with this numbers : ")
print ("1.Addition\n2.Subraction\n3.Multiplication\n4.Division")
c = input ("no. : ")

if c=="1":
    print ("sum = ", int(a) + int(b))

elif c=="2":
    print ("subraction = ",int(a) - int(b))

elif c=="3":
    print ("multiplication = ",int(a) * int(b))

elif c=="4":
    print ("Division = ",int(a) / int(b))

else:
    print ("This no. don't have any funtion")
'''

import tkinter 
from tkinter import *
from tkinter import messagebox 

#Button commands - what to do when a button is clicked.
val = ""
A = 0
operator = ""

def btn1_isclick():
    global val
    val = val + "1"
    data.set(val)

def btn2_isclick():
    global val
    val = val + "2"
    data.set(val)

def btn3_isclick():
    global val
    val = val + "3"
    data.set(val)

def btn4_isclick():
    global val
    val = val + "4"
    data.set(val)

def btn5_isclick():
    global val
    val = val + "5"
    data.set(val)

def btn6_isclick():
    global val
    val = val + "6"
    data.set(val)

def btn7_isclick():
    global val
    val = val + "7"
    data.set(val)

def btn8_isclick():
    global val
    val = val + "8"
    data.set(val)

def btn9_isclick():
    global val
    val = val + "9"
    data.set(val)

def btn0_isclick():
    global val
    val = val + "0"
    data.set(val)


def btn_plus_clicked():
    global A
    global operator
    global val 
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator
    global val 
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multi_clicked():
    global A
    global operator
    global val 
    A = int(val)
    operator = "*"
    val = val + "x"
    data.set(val)

def btn_divide_clicked():
    global A
    global operator
    global val 
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def c_pressed():
    global A 
    global operator 
    global val
    val = ""
    A = 0 
    operator = ""
    data.set(val)


def result():
    global val
    global operator
    global A
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x 
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val2.split("x")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Not Defined")
            A = ""
            val = ""
            data.set(val)
        else:
            C = float(A / x) 
            data.set(C)
            val = str(C)




root = tkinter.Tk()
root.geometry("250x400+300+300") #dimentions+X,Yaxis location
root.resizable() #should be able to resize. (0,0)-can not resize
root.title("Calculator") #title

#screen
data = StringVar()
screen = Label(
    root,
    text = "Lable",
    anchor = E, #Where lable should be placed , E = east, gives direction
    font = ("verdana", 20),
    textvariable = data,
    background = "#ffffff", #ffffff is color white
    fg = "#000000",
)
screen.pack(expand = True, fill = "both",)

#creating frame
row1 = Frame(root)
row1.pack(expand = True, fill = "both",) 
#should it expand when we resize and fill on both sides equal
row2 = Frame(root)
row2.pack(expand = True, fill = "both",)

row3 = Frame(root)
row3.pack(expand = True, fill = "both",)

row4 = Frame(root)
row4.pack(expand = True, fill = "both",)

#creating Buttons
btn1 = Button(
    row1,
    text = "1", #text to display on the button
    font = ("Verdana",22), #("font style",size)
    border = 0,
    command = btn1_isclick,
)
btn1.pack(side = LEFT , expand = True, fill = "both",) #start alling from lift side
btn2 = Button(
    row1,
    text = "2",
    font = ("Verdana",22),
    border = 0,
    command = btn2_isclick,
)
btn2.pack(side = LEFT , expand = True, fill = "both",)
btn3 = Button(
    row1,
    text = "3",
    font = ("Verdana",22),
    border = 0,
    command = btn3_isclick,
)
btn3.pack(side = LEFT , expand = True, fill = "both",)
btn4 = Button(
    row1,
    text = "+",
    font = ("Verdana",22),
    border = 0,
    command = btn_plus_clicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both",)

#Button for second row
btn1 = Button(
    row2,
    text = "4",
    font = ("Verdana",22),
    border = 0,
    command = btn4_isclick,
)
btn1.pack(side = LEFT , expand = True, fill = "both",)
btn2 = Button(
    row2,
    text = "5",
    font = ("Verdana",22),
    border = 0,
    command = btn5_isclick,
)
btn2.pack(side = LEFT , expand = True, fill = "both",)
btn3 = Button(
    row2,
    text = "6",
    font = ("Verdana",22),
    border = 0,
    command = btn6_isclick,
)
btn3.pack(side = LEFT , expand = True, fill = "both",)
btn4 = Button(
    row2,
    text = "-",
    font = ("Verdana",22),
    border = 0,
    command = btn_minus_clicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both",)

#Buttons for third row 
btn1 = Button(
    row3,
    text = "7",
    font = ("Verdana",22),
    border = 0,
    command = btn7_isclick,
)
btn1.pack(side = LEFT , expand = True, fill = "both",)
btn2 = Button(
    row3,
    text = "8",
    font = ("Verdana",22),
    border = 0,
    command = btn8_isclick,
)
btn2.pack(side = LEFT , expand = True, fill = "both",)
btn3 = Button(
    row3,
    text = "9",
    font = ("Verdana",22),
    border = 0,
    command = btn9_isclick,
)
btn3.pack(side = LEFT , expand = True, fill = "both",)
btn4 = Button(
    row3,
    text = "*",
    font = ("Verdana",22),
    border = 0,
    command = btn_multi_clicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both",)

#Button for forth row 
btn1 = Button(
    row4,
    text = "C",
    font = ("Verdana",22),
    border = 0,
    command = c_pressed,
)
btn1.pack(side = LEFT , expand = True, fill = "both",)
btn2 = Button(
    row4,
    text = "0",
    font = ("Verdana",22),
    border = 0,
    command = btn0_isclick,
)
btn2.pack(side = LEFT , expand = True, fill = "both",)
btn3 = Button(
    row4,
    text = "=",
    font = ("Verdana",22),
    border = 0,
    command = result,
)
btn3.pack(side = LEFT , expand = True, fill = "both",)
btn4 = Button(
    row4,
    text = "/",
    font = ("Verdana",22),
    border = 0,
    command = btn_divide_clicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both",)

root.mainloop()


