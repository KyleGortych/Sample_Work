"""
A text to speech script

Maintainer: Kyle Gortych
Date:       01-19-2022
"""
import sys
import pyttsx3

tts = pyttsx3.init()

print('Text to speech by Kyle Gort as by Al Sweigart')
print('Uses pyttsx3 module, which uses the os\'s NSSpeechSythesizer')
print()
print('Enter text for audio output, or QUIT to quit.')
while True:
    text = input('> ')
    if text.upper() == 'QUIT':
        print('Bye.')
        sys.exit()

    tts.say(text)
    tts.runAndWait()
