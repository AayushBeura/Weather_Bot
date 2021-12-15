# importing library
from typing import Text
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from bs4 import BeautifulSoup
from playsound import playsound
import requests
 
# enter city name
city = "jagamara"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]
 
# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]
 
# printing all data
a = "The temperature outside is " + temp
b= "The current time is " + time
c= "Describing the sky, it is " + sky

print(a)
speak(a)
print(b)
speak(b)
print(c)
speak(c)


#end of program ------