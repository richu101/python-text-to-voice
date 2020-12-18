from pygame import mixer
<<<<<<< HEAD


mixer.init()

# Loading the song/

def play_music(voice):
    """
    This function is to play the drum audios in the drum sound audios

    """
    mixer.music.load(voice)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()
=======
from gtts import gTTS
>>>>>>> 00af40d5334070fe61447e6949854c7bf264cd8e

#text to speech
text='hello'                
tts = gTTS(text, lang='en') 
tts.save('file.mp3')

<<<<<<< HEAD
# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")   
    query = input(" ")
    
    play_music(voice)
    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

=======
mixer.init()

voice=r'file.mp3'
# Calling the file to voice 

def play_music(voice):
   
    """
    This function is to play the drum audios in the drum sound audios
    """
    mixer.music.load(voice)

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    play_music(voice)
    query = input(" ")
    
   
    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

>>>>>>> 00af40d5334070fe61447e6949854c7bf264cd8e
        # Stop the mixer
        mixer.music.stop()
        break
