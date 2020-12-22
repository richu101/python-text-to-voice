from pygame import mixer
from gtts import gTTS

#text to speech


mixer.init()

voice=r'file.mp3'
# Calling the file to voice 

def play_music(voice):
   
    """
    This function is to play the audios 
    """
    mixer.music.load(voice)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()
    while True:
        
        query = input("Press p to pause, r to resume, e to exit")
        
    
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



# infinite loop
while True:

    text = input("Input the text to read: ")                    
    tts = gTTS(text, lang='en') 
    tts.save('file.mp3')
    play_music(voice)
    
