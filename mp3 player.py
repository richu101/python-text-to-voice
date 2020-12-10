from pygame import mixer

i = 0.5
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("1ds.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
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

    elif query == 'v':   
        # Volume control
        volin = input(" <- Arrow key to volume down & - -> Arrow key to volume up ")
        if volin == "^[[C":            
            i += .1
            print("volume =")
            print(i)
            mixer.music.set_volume(i) 
            if i >= 1 :
                i == .9
                print("You are at max volume")
        elif volin == "^[[D":            
            i -= .1
            print("volume =")
            print(i)
            mixer.music.set_volume(i) 
            if i <= 0 :
                i == .1
                print("You are at min volume")