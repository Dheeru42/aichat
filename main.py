import datetime
import os
import speech_recognition as sr
import win32com.client as wincom
import webbrowser
import time
import random
import openai


def ai(prompt):
    openai.api_key = "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"
    text = f"Open Ai response for prompt : {prompt}\n**********************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "prompt"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]

    if not os.path.exists("Openai files"):
        os.mkdir("Openai files")

    with open(f"Openai files/prompt - {random.randint(1,25382563898278)}","w") as f:
        f.write(text)
def say(text):   # function for saying something
    speak = wincom.Dispatch("sapi.spVoice")
    speak.Speak(f"{text}")

def takecommand():  # enabling microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing Your Voice ....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return(query)
        except Exception as e:
            return("SORRY!!!. SAY AGAIN")

if __name__ == '__main__':
    say("RAM AI CHAT")
    while 1:
        print("Listening.......")
        query = takecommand()
        # say(query)
        sites = [["Youtube", "https://www.youtube.com"]
            , ["wikipedia", "https://www.wikipedia.com"]
            , ["google", "https://www.google.com"]]

        for site in sites:  # open sites
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} bajke {minute}")

        if "ai".lower() in query.lower():
            ai(prompt=query)

