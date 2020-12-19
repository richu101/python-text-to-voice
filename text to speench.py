from pygame import mixer
from gtts import gTTS

mixer.init()
voice=r'file.mp3'

def tempfile():                                 
    tts = gTTS('hello', lang='en')
    tts.save('hello.mp3')
    return 'hello.mp3'

def play_music(voice,vol=0.7):
   
    """
    This function is to play the audios file
    """
    mixer.music.load(voice)

    # Setting the volume
    mixer.music.set_volume(vol)

    # Start playing the song
    mixer.music.play()

def  menu():
    play_music(voice)

    #infinite loop
    while True:
        
        print("Press 'p' to pause, 'r' to resume the speech")
        print("Press 'e' to exit the program")
        query = input(" ")
    
        if query == 'p':

            # Pausing the music
            mixer.music.pause()
        elif query == 'r':

            # Resuming the music
            mixer.music.unpause()
        elif query == 'e':

            # Stop the mixer
            mixer.music.stop()
            break
    
    #temporary pass
    play_music(tempfile(),0)

# infinite loop
while True:

    text = input('Enter the text to be read: ')
    
    #Converts the user input text to speech
    tts = gTTS(text, lang='en')

    #saves as file.mp3
    tts.save('file.mp3')
    
    menu()
    ch=input("Would you like to convert another text (y/n)?...")
    if ch == 'y' or ch == 'Y':
        continue
    else:
        break