from tkinter import *
from time import strftime
import math

# This calculator program was created by Black Dolphin with the email 99.
# All the code for this program was written by the owner individual and has not been copied or taken from anywhere else.
# This program separates multi-digit numbers in the output with commas. It performs addition, subtraction, and other operations.
# The program is capable of saving all calculations in its history and can continue using previous calculations as long as it hasn't been closed.
# It also supports features like calculating square roots, absolute values, and raising numbers to a power.
# Additionally, it can display the exact date and time of the calculations performed.

Results = []
# This is to create the root window
root = Tk()
root.title("Calculator")

root.geometry("517x448+500+200")
root.minsize(517,448)
root.maxsize(517,448)
#Main window such Frame
Mainf = Frame(root, bg = "white",bd=7,relief="ridge" )
Mainf.pack(fill="both",expand=False)

menu = Menu(Mainf)
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_separator()

#This Frame is parent of Label1 ,Head window for date and time
label_a = Frame(Mainf ,bg = "white",bd=7,relief="ridge" )
label_a.pack(fill="x")
#This Frame is parent of TextDisplay 
label_b= Frame(Mainf ,bg = "white",bd=7,relief="ridge", height=100 )
label_b.pack(fill="x" )
#This Frame is parent of { ↩ ,  ↻, abs , ( , ) } Buttons
label_d = Frame(Mainf ,bg = "light gray" ,relief="flat")
label_d.pack(fill="x" , expand=True )
#This frame is for left vertical math operators
label_L = Frame(Mainf ,bg = "light gray" ,relief="flat")
label_L.pack(side=LEFT,fill="both",expand=True)
#This frame is for Main numbers for calculation
label_c = Frame(Mainf, bd=7 ,relief="flat")
label_c.pack(fill="both" , expand=True )
#This is a fanction for show time
def Time():
    string_Time = strftime("%H:%M:%S")
    label1.config(text=string_Time ,font=("calibri" ,20) , bd=7 ) 
    label1.after(1000 , Time) #A recursive function , It is updated once every 1000 milliseconds
#This is a fanction for show date 
def Date():
    string_Time = strftime("20%y / %m / %d") #2024 / M / Day
    label2.config(text=string_Time ,font=("calibri" ,14) , bd = 7 )
# This is a Label for object time
label1 =  Label(label_a , font="calibri"  , bg = "Lightblue", fg="gray", relief="groove" ) 
label1.grid(row=0 , column=0  , ipadx=70)
# This is a label for object date
label2 = Label(label_a , font="calibri" , bg = "Lightblue" , fg="gray" , relief="groove" ) 
label2.grid(row=0 ,column=1 , ipadx=55 , ipady=4, sticky="e")

# setup a value for calculation_finish 
calculation_finish = False
history_list = [] # A list for calculations done
#Main Calculation 
def Maincalc():
    global calculation_finish 
    global history_list
    global Results
    try:
        if txtDisplay.get() != "": #check txtdisplay is empty or no
            if txtDisplay.get()[-1] not in ["-", "×", "+", "÷" , "^" ]: #check if befor "=" there  ["-", "×", "+", "÷" , "^"] or no 
                symbol = txtDisplay.get() # a variable for save txtdisplay.get()
                #replace math symbol to machine symbol 
                replaced = symbol.replace("^" , "**").replace("," , "").replace("×" , "*" ).replace("%" , "/100").replace("÷" , "/")
                # after 10ms txtDisplay will be destroyed
                txtDisplay.after(10 , txtDisplay.delete(0,END))
                #clacute abs if not exist any thing in display
                if replaced[0:4] == "abs(":
                    selected_rps = replaced[4:-1]
                    if eval(selected_rps) <= 0:
                        answer_abs = (-1)*eval(selected_rps)
                        txtDisplay.insert(END,f"{answer_abs:,}")
                    else:
                        txtDisplay.insert(END,f"{(eval(selected_rps)):,}")
                # else if we didn't calcute abs we use this:
                else:
                    result = (round(float(eval(replaced)) , 6))
                    txtDisplay.insert(END,f"{result:,}")
                    history_list.append(f"{symbol} = {result:,} : {strftime("%H:%M:%S")} ")
                    Results.append(symbol)
                    calculation_finish = True

    except Exception as ex:
        txtDisplay.insert(END , "ERROR something wrong")

def Add_Display(i):
    global Results
    txtDisplay.delete(0 ,END)
    txtDisplay.insert(END, Results[i])

def History():
    global history_list
    # create new window
    new_window = Toplevel(root)
    new_window.title("History List")
    new_window.geometry("300x200+200+250")
    F1 = Frame(new_window, bg="white", bd=7, relief="ridge")
    F1.pack()

    Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

    # Add widgets in new window
    for i, item in enumerate(history_list):
        Button(F1, text=f"{i+1}) {item}", command=lambda i=i:  Add_Display(i)).pack()


               

def add_plus():
    global calculation_finish
    if txtDisplay.get() != "":
        if calculation_finish:
            previous_value = txtDisplay.get()
            txtDisplay.delete(0, END) 
            txtDisplay.insert(END, previous_value + "+")  
            calculation_finish = False  
        else:
            if txtDisplay.get()[-1] in ["-", "×", "+", "÷" , "^"]:
                txtDisplay.delete(len(txtDisplay.get()) - 1, END)
                txtDisplay.insert(END, "+")
            else:
                txtDisplay.insert(END, "+")  

def clear_display_if_finished():
    global calculation_finish
    if calculation_finish:
        txtDisplay.delete(0, END)
        calculation_finish = False
click_count = 0
def add_one():
    clear_display_if_finished()
    global click_count
    click_count += 1
    txtDisplay.insert(END, "1" * click_count) 
    click_count -=1

click_count1 = 0
def add_2():
    clear_display_if_finished()
    global click_count1
    click_count1 += 1
    txtDisplay.insert(END, "2" * click_count1)
    click_count1 -=1
click_count2 = 0
def add_3():
    clear_display_if_finished()
    global click_count2
    click_count2 += 1
    txtDisplay.insert(END, "3" * click_count2)
    click_count2 -= 1
click_count3 = 0
def add_4():
    clear_display_if_finished()
    global click_count3
    click_count3 += 1
    txtDisplay.insert(END, "4" * click_count3)
    click_count3 -= 1
click_count4 = 0
def add_5():
    clear_display_if_finished()
    global click_count4
    click_count4 += 1
    txtDisplay.insert(END, "5" * click_count4)
    click_count4 -= 1
click_count6 = 0
def add_6():
    clear_display_if_finished()
    global click_count6
    click_count6 += 1
    txtDisplay.insert(END, "6" * click_count6)
    click_count6 -= 1
click_count7 = 0
def add_7():
    clear_display_if_finished()
    global click_count7
    click_count7 += 1
    txtDisplay.insert(END, "7" * click_count7)
    click_count7 -= 1
click_count8 = 0

def add_8():
    clear_display_if_finished()
    global click_count8
    click_count8 += 1
    txtDisplay.insert(END, "8" * click_count8)
    click_count8 -= 1
click_count9 = 0
def add_9():
    clear_display_if_finished()
    global click_count9
    click_count9 += 1
    txtDisplay.insert(END, "9" * click_count9)
    click_count9 -= 1
click_count0 = 0
def add_0():
    global click_count0
    click_count0 += 1
    txtDisplay.insert(END, "0" * click_count0)
    click_count0 -= 1

def add_mines():
    global calculation_finish
    if txtDisplay.get() != "":
        if calculation_finish:  # if past caculation finished
            previous_value = txtDisplay.get()  # save befor value
            txtDisplay.delete(0, END)  # delet display
            txtDisplay.insert(END, previous_value + "-")  # show mines symbol
            calculation_finish = False  # Reset the finished calculation status
        else:
            if txtDisplay.get()[-1] in ["-", "×", "+", "÷" , "^"]:
                txtDisplay.delete(len(txtDisplay.get()) - 1, END)
                txtDisplay.insert(END, "-")
            else:
                txtDisplay.insert(END, "-")  

def add_division():
    global calculation_finish
    #if txtdisplay is clear
    if txtDisplay.get() != "":
        if calculation_finish: # if past caculation finished
            previous_value = txtDisplay.get() # save befor value
            txtDisplay.delete(0, END)   # delet display
            txtDisplay.insert(END, previous_value + "÷") # show mines symbol
            calculation_finish = False  # Reset the finished calculation status
        else:
            #if the last of character == -+or... the first delet it and insert ÷ 
            if txtDisplay.get()[-1] in ["-", "×", "+", "÷" , "^"]:
                txtDisplay.delete(len(txtDisplay.get()) - 1, END)
                txtDisplay.insert(END, "÷")
            else:
                txtDisplay.insert(END, "÷")  

def add_point():
    if txtDisplay.get() == "":
        txtDisplay.insert(END, "0." )
    elif txtDisplay.get()[-1] in  ["-", "×", "+", "÷" , "^"]:
        if txtDisplay.get()[-1].isdigit():
            txtDisplay.insert(END, "." )
        else:
            txtDisplay.insert(END, "0." )
    else:
        txtDisplay.insert(END, "." )


def add_x():
    global calculation_finish
    if txtDisplay.get() != "":
        if calculation_finish:# if past caculation finished
            previous_value = txtDisplay.get() # save befor value
            txtDisplay.delete(0, END)  # delet display
            txtDisplay.insert(END, previous_value + "×")# show mines symbol
            calculation_finish = False# Reset the finished calculation status
        else:
             #if the last of character == -+or... the first delet it and insert x
            if txtDisplay.get()[-1] in ["-", "×", "+", "÷" , "^"]:
                txtDisplay.delete(len(txtDisplay.get()) - 1, END)
                txtDisplay.insert(END, "×")
            else:
                txtDisplay.insert(END, "×")  


txtDisplay = Entry(label_b, font=('arial', 30, 'bold'), bd=21, insertwidth=4, bg='light blue' , relief="sunken" )
txtDisplay.grid()
scrollbar_x = Scrollbar(label_b, orient=HORIZONTAL, command=txtDisplay.xview)
scrollbar_x.grid(row=1, column=0, sticky="ew")
def clear_all():
    clear_display_if_finished()
    txtDisplay.delete(0 , END)
def abs():
    global Results
    if txtDisplay.get() != "":
        if calculation_finish:
            previous_value = txtDisplay.get().replace("," , "")
            txtDisplay.delete(0, END)
            if float(previous_value) > 0:
                txtDisplay.insert(END, float(previous_value))
            else:
                calc_abs = eval(str((-1)*float(previous_value)))
                txtDisplay.insert(END, calc_abs)
                Results.append(previous_value)
                history_list.append(f"{previous_value} = {calc_abs:,}")
                
        else:
            pass
    else:
        txtDisplay.insert(END , "abs(")
        if txtDisplay.get()[-1] == ")":
            Maincalc()*(-1)
def power():
    global calculation_finish
    if txtDisplay.get() != "":
        if calculation_finish:# if past caculation finished
            previous_value = txtDisplay.get() # save befor value
            txtDisplay.delete(0, END)  # delet display
            txtDisplay.insert(END, previous_value + "^") # show mines symbol
            calculation_finish = False# Reset the finished calculation status
        else:
            if txtDisplay.get()[-1] in ["-", "×", "+", "÷" , "^"]:
                txtDisplay.delete(len(txtDisplay.get()) - 1, END)
                txtDisplay.insert(END, "^")
            else:
                txtDisplay.insert(END, "^")

def sqrt():
    global history_list
    sqr = txtDisplay.get().replace("," , "")
    txtDisplay.delete(0,END)
    try:
        calc = eval(str(sqr))
        sq = math.sqrt(calc)
        txtDisplay.after(1 , txtDisplay.insert(END,f"{sq:,}"))
        history_list.append(f"{calc} = {sq:,}")
    except ValueError:
        #if under the radical negetive:
        txtDisplay.delete(0,END)
        txtDisplay.insert(END, "Unvalid")
Button(label_d , text="(" , font=("Tahoma", 15) , width=6 , command=lambda:txtDisplay.insert(END, "(" ),relief="flat", bg="light gray").grid(row=1,column=1, ipadx=11)
Button(label_d , text=")" , font=("Tahoma", 15)  , width=6 , command=lambda:txtDisplay.insert(END, ")" ),relief="flat", bg="light gray").grid(row=1,column=2, ipadx=11)
Button(label_d , text="abs" , font=("Tahoma", 15) , width=4 , command=abs,relief="flat", bg="light gray").grid(row=1,column=3, ipadx=11)
Button(label_d , text="↻" , font=("Tahoma", 15)  , width=6 , command=clear_all,relief="flat", bg="light gray").grid(row=1,column=4, ipadx=11)
Button(label_d , text="↩" , font=("Tahoma", 15) , width=10, command=lambda:txtDisplay.delete(len(txtDisplay.get())-1 , END),relief="flat", bg="light gray").grid(row=1,column=5, ipadx=16)
Button(label_L , text="√" , font=("Tahoma", 10)  , width=10 , command=sqrt ,relief="flat" , bg="light gray").grid(row=0,column=0,pady=2,ipady=10,ipadx=8)
Button(label_L , text="X^n" , font=("Tahoma", 10)  , width=10 , command=power,relief="flat", bg="light gray").grid(row=1,column=0 ,pady=2,ipady=10,ipadx=8)
Button(label_L , text="%" , font=("Tahoma", 10) , width=10 , command=lambda:txtDisplay.insert(END,"%"),relief="flat", bg="light gray").grid(row=2,column=0,pady=2,ipady=10,ipadx=9)
Button(label_L , text="HISTORY" , font=("Tahoma", 10) , width=10 , command=History,relief="flat", bg="light gray").grid(row=3,column=0,pady=2,ipady=10,ipadx=9)

Button(label_c , text="1" , font=("Tahoma", 15)  , width=4 , command=add_one,relief="flat" ).grid(row=0,column=0 ,ipadx=20 , pady=10)
Button(label_c , text="2" , font=("Tahoma", 15)  , width=4 , command=add_2,relief="flat" ).grid(row=0,column=1,ipadx=20)
Button(label_c , text="3" , font=("Tahoma", 15)  , width=4 , command=add_3,relief="flat").grid(row=0,column=2,ipadx=20)
Button(label_c , text="+" , font=("Tahoma", 15)  , width=6 , command=add_plus,relief="flat" ).grid(row=0,column=3,ipadx=20)
Button(label_c , text="4" , font=("Tahoma", 15)  , width=4 , command=add_4,relief="flat").grid(row=1,column=0,ipadx=20)
Button(label_c , text="5" , font=("Tahoma", 15)  , width=4 , command=add_5,relief="flat" ).grid(row=1,column=1,ipadx=20)
Button(label_c , text="6" , font=("Tahoma", 15)  , width=4 , command=add_6,relief="flat").grid(row=1,column=2,ipadx=20)
Button(label_c , text="-" , font=("Tahoma", 15)  , width=6 , command=add_mines,relief="flat").grid(row=1,column=3,ipadx=20)
Button(label_c , text="7" , font=("Tahoma", 15)  , width=4 , command=add_7,relief="flat" ).grid(row=2,column=0,ipadx=20)
Button(label_c , text="8" , font=("Tahoma", 15)  , width=4 , command=add_8,relief="flat").grid(row=2,column=1,ipadx=20)
Button(label_c , text="9" , font=("Tahoma", 15)  , width=4 , command=add_9,relief="flat" ).grid(row=2,column=2,ipadx=20)
Button(label_c , text="÷" , font=("Tahoma", 15)  , width=6 , command=add_division,relief="flat").grid(row=2,column=3,ipadx=20)
Button(label_c , text="0" , font=("Tahoma", 15)  , width=4 , command=add_0,relief="flat").grid(row=3,column=0,padx="5",ipadx=20, pady="5")
Button(label_c , text="." , font=("Tahoma", 15)  , width=4 , command=add_point,relief="flat").grid(row=3,column=1,padx="5", pady="5")
Button(label_c , text="=" , font=("Tahoma", 15)  , width=4 , command=Maincalc,relief="flat").grid(row=3,column=2,padx="5",ipadx=20, pady="5")
Button(label_c , text="×" , font=("Tahoma", 15)  , width=6 , command=add_x,relief="flat").grid(ipadx=20,row=3,column=3,padx="5", pady="5")

Time()
Date()



root.mainloop()