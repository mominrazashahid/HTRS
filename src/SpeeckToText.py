import speech_recognition as sr
from gtts import gTTS
import pycountry
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def speech_to_text(CountryCode):
# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=4)
    try:
        response = r.recognize_google(audio,language=CountryCode+'-IN')
        return response
        # tts = gTTS(text="I think you said " + str(response), lang='en')
        # tts.save("response.mp3")
        # mixer.music.load('response.mp3')
        # mixer.music.play()
    except sr.UnknownValueError:
        return "Sphinx could not understand audio"
    except sr.RequestError as e:
        error=("error")
        return error
