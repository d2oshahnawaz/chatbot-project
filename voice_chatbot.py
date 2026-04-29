import speech_recognition as sr
import pyttsx3
import random
from train_model import predict_intent
from chatbot_model import responses

# text to speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# speech to text
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        print("Sorry, could not understand.")
        return ""

# main loop
while True:
    user_input = listen()

    if user_input in ["bye", "exit", "quit"]:
        speak("Goodbye!")
        break

    intent = predict_intent(user_input)

    if intent in responses:
        reply = random.choice(responses[intent])
    else:
        reply = "Sorry, I don't understand."

    print("Bot:", reply)
    speak(reply)