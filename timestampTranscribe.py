import speech_recognition as sr
import time

inp = input("Input audio filename: ")
lis = input("Duration of audio to transcribe: ")
fre = input("Timestamp Frequency: ")
out = input("Output filename (do not include .csv): ")

def transcribe(inputAudio,listeningTime,frequency,outputFilename):
    '''
    timestampTranscribe transcribes a wav file by the given frequency
    
    inputAudio is a string input, the audio to transcribe (.wav)
    listeningTime is an int, the length of the audio you want to transcribe
       - trying to find a way to automate this parameter
    frequency is an int, how often the timestamp should log
    outputFileName is a string of the csv file's output name    
    '''
    f = open(outputFilename+".csv","w") # open output file to write to
    sound = sr.AudioFile(inputAudio) # open audio
    
    r = sr.Recognizer() # recognizer object
    snips = [] # array to store all the audio snips if you need them
        
    with sound as source:
        second = 0
        
        while second<listeningTime:
            audio = r.record(source,duration=frequency)
            
            try:# recognized text, output to console
                text = r.recognize_google(audio)
                print("recognized: \""+ text +"\" at "+str(second)+" seconds")
            
            except sr.UnknownValueError:# no speaking makes an error
                text = "-"
            
            snips.append(text if text!="-" else None) 
            f.write(str(second) + "," + text + "\n")# write timestamp+transcribe
            
            second+=frequency# move to the next snip of audio  
            time.sleep(0.5)
    
    f.close()
    
transcribe(inp,int(lis),int(fre),out)
print("done")