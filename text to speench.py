from pygame import mixer


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

        # Stop the mixer
        mixer.music.stop()
        break
