import requests
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('rate', 175)

def take_input():
	with mic as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	speech = r.recognize_google(audio)
	return speech

def text_to_speech(text):
	engine.say(text)
	engine.runAndWait()
	engine.stop()


print("Waiting for input:")
voice_input = take_input()
print(voice_input + "\n")

while True:
	if "joke" in voice_input or "funny" in voice_input:
		response = requests.get('https://icanhazdadjoke.com', headers={'Accept':'application/json'})
		joke = response.json()['joke']
		print(joke)
		text_to_speech(joke)
		continue

	if "close" in voice_input or "quit" in voice_input:
		engine.stop()
		exit()
	engine.stop()