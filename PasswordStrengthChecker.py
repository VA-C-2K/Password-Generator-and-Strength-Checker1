from tkinter import *
import re

t = Tk()
t.geometry('500x100+700+250')
t.title('Password Checker')
guiFont = font = dict(family='Courier New, monospaced',size=18, color='#7f7f7f')

eLable = Label(t,text="Please Enter your Password:  ",font=guiFont)
ePassword = Entry(t,show='*')
ePassword.grid(row=0,column=1)

def checkpassword():
    strength=['Password can not be empty','Weak','Medium','Strong','Very Strong']
    score = 1
    password = ePassword.get()
    print(password, len(password))

    if len(password) == 0:
        passwordStrength.set(strength[0])
        return
    if len(password) < 4:
        passwordStrength.set(strength[1])
        return 
    if len(password) >=8:
        score +=1
    if re.search("[0-9]",password):
        score+=1
    if re.search("[a-z]",password) and re.search("[A-Z]",password):
        score+=1 
    if re.search(".",password):
        score+=1
    
    passwordStrength.set(strength[score])


passwordStrength = StringVar()
checkStrBtn = Button(t,text="Check Strength",command= checkpassword,height=1,width=15,font=guiFont)
checkStrBtn.grid(row=2,column=0)
checkstrLab = Label(t,textvariable = passwordStrength)
checkstrLab.grid(row=2,column=1,sticky=W)
t.mainloop()
