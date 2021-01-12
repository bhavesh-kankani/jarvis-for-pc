import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import wikipedia
import smtplib


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is..")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("today's date is..")
    speak(day)
    speak(month)
    speak(year)
def day():
    speak(calendar.day_name[datetime.date.today().weekday()])


def wishme():
    speak("Welcome ma'am")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-hi')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry I didnt understand.. could you please repeat it..")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.ehlo()
    server.starttls()
    server.login('bhaveshkankani769@gmail.com', 'b.kankani..')
    server.sendmail('bhaveshkankani769@gmail.com', to , content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'day' in query:
            day()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences = 2)
            speak("search complete")
            print(result)
            speak(result)
        elif 'email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                recipient_mail = "komal.k.kankani@gmail.com"
                speak("trying to send the email")
                sendEmail(recipient_mail, content)
                speak("Email sent successfully.")
            except Exception as e:
                print(e)
                speak("Some error has occured.. Unable to send the email")
        elif 'go offline' in query:
            speak("going offline")
            quit()