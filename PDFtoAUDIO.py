# Omar Faruk Badhon
# Email: omarfarukbadhon@gmail.com

# Import Library for this project 
import PyPDF2
import pyttsx3
from gtts import gTTS
import playsound
import os
from bs4 import BeautifulSoup


open_pdf = open(r'H:\PYTHON\Project\Pdf to Audio\Python.pdf', 'rb') #Open file for read (rb)
convert_text = PyPDF2.PdfReader(open_pdf)
text_file = ""

# Count total page number of a file
for pageNum in range(len(convert_text.pages)):
    pageObj = convert_text.pages[pageNum]
    text_file += pageObj.extract_text()

open_pdf.close()
voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0' # Set your system voice 
engine = pyttsx3.init()
engine.setProperty('rate', 200) # Set Voice speed 
engine.setProperty('voice', voice_id)
engine.say(text_file)
engine.runAndWait()
tts = gTTS(text=text_file, lang='en')
tts.save("Python.mp3")
os.system("mpg321 Python.mp3")
playsound.playsound('Python.mp3', True)


