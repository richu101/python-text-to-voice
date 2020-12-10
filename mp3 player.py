from pygame import mixer

i = 0.5
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load('/home/pi/Documents/python/Text-to-Speech/1ds.mp3')

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("press 'v' to enter volume control mode")
    query = input(" ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'v':
        # Volume control
        volin = input("press D to volume down & U to volume up ")
        c = 'n' # to enter the volume control loop
        while c != "ex":
           # print(" Volume UP or Down")
            if volin == "u":
                if i <= 1:
                    i += .1
                    print("volume UP=")
                    print(i)
                else:
                    i = .9    
                    print("You are at max volume")
    
                mixer.music.set_volume(i)
                
            if volin == "d":
                if i > 0 :
                    i -= .1
                    print("volume DOWN=")
                    print(i)
                else:
                    i = 0    
                    print("You are at min volume")
    
                mixer.music.set_volume(i)
            volin = input("")
            c = volin

    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
