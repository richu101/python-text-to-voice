from pygame import mixer 

i = 0.5
# Starting the mixer 
mixer.init() 

# Loading the song 
mixer.music.load("hello.mp3") 

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
        
    # Volume control
    elif querry == 'v'
        volin = input(" Press -> arrow to volume UP and <- Arrow to volume down")
        if volin == "^[[C":            
            i += .1
            mixer.music.set_volume(i) 
            if i >= 1 :
                i == .9
                print("You are at max volume")
        elif volin == "^[[C":            
            i -= .1
            mixer.music.set_volume(i) 
            if i <= 0 :
                i == .9
                print("You are at min volume")
    # mixer.music.play() 
	elif query == 'e': 

		# Stop the mixer 
		mixer.music.stop() 
		break




^[[D

