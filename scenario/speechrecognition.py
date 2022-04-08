from wave import Wave_write
import speech_recognition as sr
from os import path 
import os
import utils 
def speech_recognition(args):
    r = sr.Recognizer()
    wav_file = [i for i in os.listdir(os.path.join(args.data_dir,'common_voice','wav'))]
    #print('wav_file lenght',len(wav_file))
    ftest = open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'w')
    for i in wav_file:
        Audio_file = os.path.join(args.data_dir,'common_voice','wav',i)
        AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), "english.wav")
        with sr.AudioFile(Audio_file) as source:
            audio = r.record(source) 
        #ftest = open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'w')
        
        try:
            transcription = r.recognize_google(audio,language='vi-VN')
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`

            print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language='vi-VN'))
            ftest.write(f'{i}\t{transcription}\n')
            #continue

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            ftest.write(f'{i}\t \n')
            #continue
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

    
        