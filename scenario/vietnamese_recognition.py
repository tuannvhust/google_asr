from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from datasets import load_dataset
import soundfile as sf
import torch
import os
# load model and tokenizer
def vietnamese_recognition(args):

    processor = Wav2Vec2Processor.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
    model = Wav2Vec2ForCTC.from_pretrained("nguyenvulebinh/wav2vec2-base-vietnamese-250h")
    wav_file = [i for i in os.listdir(os.path.join(args.data_dir,'common_voice','wav'))]
    ftest = open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'w')
    

# define function to read in sound file
    def map_to_array(batch):
        speech, _ = sf.read(batch["file"])
        batch["speech"] = speech
        return batch
    for i in wav_file:
        #ftest = open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'w')

# load dummy dataset and read soundfiles
        ds = map_to_array({
        "file": f'data/common_voice/wav/{i}'
        })

# tokenize
        input_values = processor(ds["speech"], return_tensors="pt", padding="longest").input_values  # Batch size 1

# retrieve logits
        logits = model(input_values).logits

# take argmax and decode
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)
        print('ASR thinks you said: ',transcription)
        #ftest = open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'w')
        ftest.write(f'{i}\t{transcription}\n')
    ftest.close()