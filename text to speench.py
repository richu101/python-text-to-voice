
from io import BytesIO
from gtts import gTTS
from playsound import playsound

def speak(text):
        mpe_fp = BytesIO()
        tts = gTTS(text,lang='en')
        tts.save('mp3.wav')
      #  tts.write_to_fp(mpe_fp)
      # playsound(mpe_fp)



if __name__ == '__main__' :
    print("What should i say..?")
    text = input("  > >  ")
    speak(text)

"""


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("mp3.mp3")
play(song)
"""