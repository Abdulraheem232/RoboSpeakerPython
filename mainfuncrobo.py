import pyttsx3
from tkinter import filedialog , messagebox
import os
import warnings
from gtts import gTTS


#print("-------------------------------------------")
#print("A Robospeaker 1.0 made by abdulraheem")
#print("-------------------------------------------")
def main(choice):
        emit = pyttsx3.init()
        emit.say(choice)
        emit.runAndWait()

def importfileaudio():
    # Open a file dialog to select an audio file
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    # Check if a file was selected
    if filepath:
        # Open the file and read its contents
        with open (filepath) as file:
            data = file.read()
            return data
    else:
        print("No file selected.")

def downloadvoice(voicetodownload , window):
           messagebox.showinfo(title="Info" , message="The audio u are saving will not sound like the audio you listen")
           window.withdraw()
           filepath = filedialog.asksaveasfile(defaultextension=".mp3",filetypes=[("Audio files" , ".mp3")])
           tts = gTTS(text=voicetodownload, lang='en')
           tts.save(filepath.name)
           window.deiconify()
