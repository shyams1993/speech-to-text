import speech_recognition as sr 									#import speechrecognition module & pyaudio module
r=sr.Recognizer()													#create a variable r that stores the function sr.recognizer()

with sr.Microphone()as source:										#with the microphone as source
	print("Speak: ")												#print speak so user can speak
	audio=r.listen(source)											#listen to the source speech(call the listen function using r var) & store in audio
	try: 															#exception handling -- 
		output=r.recognize_google(audio)							#listen to the audio and recognize using google's audio function
		print("You said :{}".format(output)) 						#print the output
	except:
		print("I cant recognize what you said, pls speak again") 	#if couldnt recognize, have the user repeat
