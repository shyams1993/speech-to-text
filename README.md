# speech-to-text
Python program to get speech as input and convert it to text

ALGORITHM:

#import speechrecognition module & pyaudio module
#create a variable r that stores the function sr.recognizer()
#with the microphone as source
#print speak so user can speak
#listen to the source speech(call the listen function using r var) & store in audio
#exception handling -- 
#listen to the audio and recognize using google's audio function
#print the output
#if couldnt recognize, have the user repeat


Note: 
Install both pyaudio and speechrecognition modules
if pyaudio is not installing, go to https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio,
  download the version suitable for you
    how to find the version suitable for you?
      1) in cmd, type python
      2) shows something like this (Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
      Type "help", "copyright", "credits" or "license" for more information.)
        32 bit (Intel) is my version
    Choose the correct version and download as ".whl" file
    then install the .whl file via pip command
