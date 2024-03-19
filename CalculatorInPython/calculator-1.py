from tkinter import *
#this line is for GUI

def write(x):
    s=len(start.get())
    start.insert(s,str(x))
#this function is for taking an input and writing that input on screen


calculation=7
s1=0
#that calculation variable keeps the data of operation
#first it assigned to 7,but later the value will be changed
#s1 variable is keeping the first number

def operations(x):
    global calculation
    calculation=x
    global s1
    s1=float(start.get())
    print(calculation)
    print(s1)
    start.delete(0,"end")
#this function is determines the operation
#x is the operation that the user chooses
#the value assigned to the calculation variable determines which operation to take
#The first number entered by the user is assigned to the s1 variable
#and the input part is deleted with the start.delete() method

s2=0
#s2 variable is keeping the second number

def calculate():
    global s2
    s2=float(start.get())
    print(s2)
    global calculate
    result=0
    if(calculation==0):
        result=s1+s2
    elif(calculation==1):
        result=s1-s2
    elif(calculation==2):
        result=s1*s2
    elif(calculation==3):
        result=s1/s2
    start.delete(0,"end") #deleting the first number from the screen before entering the second number
    start.insert(0,str(result))
#this functions for the calculation
#first, it assigns the second number to variable s2
#then, it performs the correct operation according
#to the calculation variable and prints the result to the screen

window=Tk() 
window.title("CALCULATOR")
window.geometry("500x500")
window.configure(bg="lightpink")
#Tk object is created from the tkinter library
#the window title is set to "CALCULATOR" 
#the size of the window is set to 500x500 pixels
#the background color is lightpink

start=Entry(font="Verdana 14 bold", width=20, justify=RIGHT)
start.place(x=80,y=20)
#this part is for taking entry
#entry part font is vernada 14 bold
#width is 2o character and it is aligned to the right

b=[]
for i  in range(1,10):
    b.append(Button(text=str(i),font="Vernada 14 bold",width=4,command=lambda x=i:write(x), bg="lightpink"))
#creates buttons that display numbers 1 through 9 and adds them to a list
#write() function is assigned to each button.

counter=0
for i in range(0,3):
    for j in range(0,3):
        b[counter].place(x=80+j*70, y=80+i*70)
        counter+=1
#this part is locationed the number boxes in order       

operation=[]
for i in range(0,4):
    operation.append(Button(fg="black",bg="blue",font="Verdana 14 bold",width=4,command=lambda x=i:operations(x)))
operation[0]["text"]="+"
operation[1]["text"]="-"
operation[2]["text"]="*"
operation[3]["text"]="/"
#it creates 4 operation boxes and adding them in a list

for i in range(0,4):
    operation[i].place(x=300,y=80+50*i)
#this is organize the operation boxes 
    
zerobutton=Button(text=0,font="Verdana 14 bold",width=4,command=lambda x=0:write(x))
zerobutton.place(x=80,y=280)
dotbutton=Button(text=".",font="Verdana 14 bold",width=4,command=lambda x=".":write(x))
dotbutton.place(x=220,y=280)
equalbutton=Button(text="=",fg="black",bg="blue",font="Verdana 14 bold",width=4,command=calculate)
equalbutton.place(x=300,y=280)
#In this section, the zero button, point button and equal button are created
#placed in the window.

window.mainloop()
#this line ensures that the window runs continuously
#the program ends when the user closes the window
