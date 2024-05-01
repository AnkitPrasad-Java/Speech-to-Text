import speech_recognition 
import pyttsx3

#initialize the recognizer
r=speech_recognition.Recognizer()

#loop in case of errors
while(True):
    try:
        #use the microphone as a source of input
        with speech_recognition.Microphone() as mic:
            #prepare recognizer to receive input
            r.adjust_for_ambient_noise(mic, duration=0.2)

            #listen for user input
            audio=r.listen(mic)

            #using google to recognize audio
            MyText=r.recognize_google(audio)
            MyTest=MyText.lower()

            print(f"Recognized {MyText}")


    except speech_recognition.UnknownValueError:
        r=speech_recognition.Recognizer()
        continue
