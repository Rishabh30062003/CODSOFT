import random, string
from tkinter import *
import pyperclip
 
 
#Initialize Window
 
root =Tk()
root.geometry("500x500") #size of the window by default
 
#title of our window
root.title("RANDOM PASSWORD GENERATOR")
 
# -------------------  Random Password generator function
 
output_pass = StringVar()
 
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  #list of all possible characters
 
def randPassGen():
    password = "" # to store password
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
 
# ----------- Copy to clipboard function
 
def copyPass():
    pyperclip.copy(output_pass.get())
 
#-----------------------Front-end Designing (GUI)
 
pass_head = Label(root, text = 'PASSWORD LENGTH', font = 'Oliviar 14 bold').pack(pady=10) #to generate label heading
 
pass_len = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = pass_len , width = 24, font='Oliviar 18').pack()
 
#Generate password button
 
Button(root, command = randPassGen, text = "GENERATE PASSWORD", font="Oliviar 10", bg='lightblue', fg='GREEN', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = Label(root, text = 'RANDOM PASSWORD GENERATED', font = 'Oliviar 12 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 24, font=' 16').pack()
 
#Copy to clipboard button
 
Button(root, text = 'COPY TO CLIPBOARD', command = copyPass, font="Oliviar 10", bg='lightblue', fg='RED', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop()  #to bundle pack