#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Description: This is a virtual assistant program that gets the date, time and responds back with a random greeting. Returns information on a person

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install Wikipedia

#Import the Libraries

import speech_recognition as sr
import wikipedia
import datetime
import os
import random
from gtts import gTTS
import warnings
import calendar
import time

#Ignore any warning messages
warnings.filterwarnings('ignore')

#Activate microphoneto listen to audio
#Record audio and return it as a string
def recordAudio():
    
    #Record the Audio
    r = sr.Recognizer() #Creating a recognizer object
    
    #open the microphone and start recording
    with sr.Microphone() as source:
        print('I am listening!')
        audio = r.listen(source)
        
    #Use Google's Speech Recognition
    data = ''
    try: 
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError: #Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error')
        
    return data

#Function for text to audio so the VA can respond
def assistantResponse(text):
    
    print (text)
        
    #Convert the text to speak
    myobj = gTTS(text= text, lang='en', slow=False)
    
    #Save the converted audio to a file
    myobj.save('assistant_response.mp3')
    
    #Play the converted file
    os.system('open assistant_response.mp3')

#A function for wake word(s) or phrase

def wakeWord(text):
    WAKE_WORDS = ['hey', 'okay']
    
    text = text.lower() #Convering text to all lower case words
    
    #Check to see if the users command/text contains a wakeword/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
        
        #if the wake word isn't found in the text from the loop and so it returns false
    return False

#A function to get the current date
def getDate():
    
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    
    #A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    #A list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    #A list of weekdays
    return 'Today is '+weekday+' '+month_names[monthNum - 1]+' the '+ordinalNumbers[dayNum-1]+'. '

#A function to return a random greeting response

def greeting(text):
    #Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'wassup', 'hello']
    #Greeting responses
    GREETING_RESPONSES = ['hi', 'hello', 'hey there', 'whats good']
    
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    #If no greeting detected, return empty string
    return ''

#A function to get a person's first and last name from the text

def getPerson(text):
    
    wordList = text.split() #Splitting the text into a list of words
    
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]
        
def getPerson2(text):
    
    wordList = text.split() #Splitting the text into a list of words
    
    for i in range(0, len(wordList)):
        if i + 2 <= len(wordList) - 1 and wordList[i].lower() == "who's":
            return wordList[i+1] + ' '+ wordList[i+2]

def getThing(text):
    
    wordList = text.split() #Splitting the text into a list of words
    
    for i in range(0, len(wordList)):
        if i + 2 <= len(wordList) - 1 and wordList[i].lower() == 'what' and wordList[i+1].lower() == 'is':
            return wordList[i+2]


while True:
    
    #Record the audio
    text = recordAudio()
    response = ''
    
    #Check for the wake words/phrase
    if(wakeWord(text) == True):
        
                 #Check for greetings
            response = response + greeting(text)
        
        #check to see if the user said anything with the date
            if('date' in text):
                get_date = getDate()
                response = response + ' '+get_date
            
            if('time' in text):
                now = datetime.datetime.now()
                meridiem = ''
                if now.hour >= 12:
                    meridiem = 'p.m'
                    hour = now.hour - 12
                else:
                    meridiem = 'a.m'
                    hour = now.hour
                    
                if now.minute < 10:
                    minute = '0'+str(now.minute)
                else:
                    minute = str(now.minute)
                
                response = response +' '+'It is '+str(hour)+ ':'+ minute+ ' '+meridiem+' .'
                    
                    
        #Check to see if the user said 'who is'
            if('who is' in text):
                person = getPerson(text)
                print(person)
                wiki = wikipedia.summary(person, sentences=2)
                response = response +' '+ wiki
            
            if("who's" in text):
                person = getPerson2(text)
                print(person)
                wiki = wikipedia.summary(person, sentences=2)
                response = response +' '+ wiki
                
            if("what is" in text):
                thing = getThing(text)
                print(thing)
                wiki = wikipedia.summary(thing, sentences=4)
                response = response +' '+ wiki
            
        #Have the assistant respond back using audio and text from response
            assistantResponse(response)
            break
            
        
    


# In[ ]:




