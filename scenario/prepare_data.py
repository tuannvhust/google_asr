import os 
from os import path
from re import A
import re
from pydub import AudioSegment
import torch.nn as nn

def prepare_data(args):
    #Check if data is dowloaded or not
    """
    if not os.path.exists(os.path.join(args.data_dir,'common_voice.zip')):
        print("downloading data...")
        os.system(f'wget -P {args.data_dir} https://docs.google.com/uc?export=download&id=1rcSWuYiDxa0ZWDVNy4WAMSf0hl3qO-YI -O common_voice.zip')
    else:
        print("skipping downloading data")
    """
    if args.extract_data:
        print("extracting data....")
        os.system(f'unzip -n -q {os.path.join(args.data_dir, "common_voice.zip")} -d {args.data_dir}')
    else:
        print("skipping extracting rir_noise")
    
    with open(os.path.join(args.data_dir,'common_voice','test.txt'),'r') as test_file:
        test_set = [line.strip('\n') for line in test_file]
    test_set = sorted(list(test_set))
    #print(test_set)
    test_list = [i.split('\t')[0] for i in test_set]
    #print(test_list)
    for file in test_list:
        os.system(f'ffmpeg -i {args.data_dir}/common_voice/mp3/{file}.mp3 -acodec pcm_s16le -ac 1 -ar 16000 {args.data_dir}/common_voice/wav/{file}.wav')
        #sound.export("/output/path/file.wav", format="wav")
    print("FINISH CONVERTING MP3 TO WAV")











 

        
    
        
