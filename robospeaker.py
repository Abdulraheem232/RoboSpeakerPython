import pyttsx3
from tkinter import *
from mainfuncrobo import main , importfileaudio , downloadvoice

window = Tk()
window.title("RoboSpeaker 1.0")
window.geometry("1000x750")
window.resizable(False,False)

def addvoiceaudio():
    choice = textinput.get("1.0", END)
    main(choice)
def showtextaudio():
    audio = importfileaudio()
    textinput.insert(END, audio)

container = Frame(window)
container.pack(expand=True)
myimage = PhotoImage(file="favicon.png" ,width=20 , height=20)
intro = Label(container , text="A robo speaker 1.1 made by abdulraheem", font=("Sans Serif" , 20 , "bold") ,image=myimage , compound="right" )
textinput  = Text(container, padx="20px" , pady="10px" , font=("Sans serif" , 15 , "bold"))
buttoncontainer = Frame(container)
submitbutton = Button(buttoncontainer,text="Listen Audio" , background="green" , fg="white" , activebackground="green" ,  activeforeground="white" , borderwidth=0 , font=("Sans Serif" , 13 , "bold") , padx="7px" , pady="7px" , command=addvoiceaudio)
importfile = Button(buttoncontainer,text="Import file" , background="blue" , fg="white" , activebackground="blue" ,  activeforeground="white" , borderwidth=0 , font=("Sans Serif" , 13 , "bold") , padx="7px" , pady="7px", command=showtextaudio)
downloadaudio = Button(buttoncontainer,text="Download audio" , background="red" , fg="white" , activebackground="red" ,  activeforeground="white" , borderwidth=0 , font=("Sans Serif" , 13 , "bold") , padx="7px" , pady="7px",command=lambda:downloadvoice(textinput.get("1.0",END) , window))

intro.grid(pady="10px")
textinput.grid()
submitbutton.grid(row=2 , padx="12px", column=0)
importfile.grid(row=2 , padx="12px",column=1)
downloadaudio.grid(row=2 , padx="12px",column=2)
buttoncontainer.grid(pady="10px")

window.mainloop()