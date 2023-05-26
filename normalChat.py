from difflib import get_close_matches
import json
from random import choice
import datetime
class DateTime:
    def currentTime(self):
        time = datetime.datetime.now()
        x = " A.M."
        if time.hour > 12: x = " P.M."
        time = str(time)
        time = time[11:16] + x
        return time

    def currentDate(self):
        now = datetime.datetime.now()
        day = now.strftime('%A')
        date = str(now)[8:10]
        month = now.strftime('%B')
        year = str(now.year)
        result = f'{day}, {date} {month}, {year}'
        return result


def wishMe():
    now = datetime.datetime.now()
    hr = now.hour
    if hr < 12:
        wish = "Good Morning"
    elif hr >= 12 and hr < 16:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"
    return wish


def isContain(text, lst):
    for word in lst:
        if word in text:
            return True
    return False


def chat(text):
    dt = DateTime()
    result = ""
    if isContain(text, ['good']):
        result = wishMe()
    elif isContain(text, ['time']):
        result = "Current Time is: " + dt.currentTime()
    elif isContain(text, ['date', 'today', 'day', 'month']):
        result = dt.currentDate()

    return result


data = {
	"how are you": [
		"Hey, I'm Good !",
		"I'm good",
		"I'm good, what about you?",
		"I'm fine, hope you're also fine",
		"Good, how about you?",
		"Doing fine, and you?",
		"I'm doing great",
		"I'm doing Well"
	],
	"what is your name": [
		"You can call me by any name",
		"Name doesn't matter",
		"I'm your Personal Assistant"
	],
	"who are you": [
		"I'm your Personal Assistant",
		"You know me right! If not then I'm your Personal Assistant",
		"You developed me, so you must know who I am",
		"Did I forget to introduce myself? I'm your Personal Assistant"
	],
	"tell me something": [
		"I have nothing to say...",
		"Hmm, you can ask me anything",
		"Hmm, you can ask me to tell a joke"
	],
	"thank you": [
		"Thank You",
		"Thank you so much",
		"Why are you saying thank you?",
		"My Pleasure",
		"You're welcome",
		"Welcome"
	],
	"hello": [
		"Hello",
		"Hello, how are you?"
	],
	"i am fine": [
		"Hope you're fine",
		"Good to know that you are fine",
		"Good to know"
	],
	"are you robot": [
		"Of course I'm a kind of Robot",
		"I'm your friend",
		"Yes I'm a robot, but I'm a good one"
	],
	"i have a question": [
		"Ask me",
		"Ask me, I can help you",
		"Don't hesitate, ask me",
		"You can always ask me"
	],
	"your birthday": [
		"I don't celebrate my Birthday",
		"My birthday is on 22nd September, 2020"
	],
	"you are funny": [
		"Good to know, that I'm funny - Haha !",
		"You think I'm funny",
		"Ya, I'm so funny",
		"I'm funny and can also make you laugh, Just ask me to tell a Joke"
	],
	"which colour you like": [
		"I like all the 7 Colors of a rainbow",
		"All Colors are my favorite"
	],
	"do you love me": [
		"Ya, I love you so much",
		"Ofcourse, I love you",
		"We're best friends"
	],
	"are you single": [
		"Haha, I'm always be single",
		"I'm your Assistant, and I dont want any relationship",
		"I'm only for you"
	],
	"you are smart": [
		"Yes, I'm smart",
		"Ofcourse I'm smart",
		"I'm a program, so I'm smart"
	],
	"i am really sorry": [
		"It's Ok",
		"No problem"
	],
	"are you my friend": [
		"Yes, I'm your friend",
		"We both are friend"
	],
	"i am alone": [
		"Don'f feel lonely. I'm always with You",
		"I can make you feely happy, Just say tell me a joke"
	],
	"i like your voice": [
		"Hope you love it...",
		"Thanks, I think this voice suits you the most",
		"Thank You So Much",
		"Ohh, that's good to know"
	]
}


def reply(query):
    if query in data:
        response = data[query]
    else:
        query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
        if len(query) == 0: return "None"
        return choice(data[query[0]])

    return choice(response)


def lang_translate(text, language):
    from googletrans import Translator, LANGUAGES
    if language in LANGUAGES.values():
        translator = Translator()
        result = translator.translate(text, src='en', dest=language)
        return result
    else:
        return "None"
