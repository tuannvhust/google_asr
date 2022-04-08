from jiwer import wer
import os
import jiwer

def WER_Measurement(args):

    with open(os.path.join(args.data_dir,'common_voice','test.txt'),'r') as test_file:
        test_set = [line.strip('\n') for line in test_file]
    test_set = sorted(list(test_set))
    ground_truth = [i.split('\t')[1] for i in test_set]


    with open(os.path.join(args.data_dir,'common_voice','google_result.txt'),'r') as ggasr_file:
        ggasr_set = [line.strip('\n') for line in ggasr_file]
    ggasr_set = sorted(list(ggasr_set))
    hypothesis = [i.split('\t')[1] for i in ggasr_set]

    print('ground_truth',ground_truth)
    print('hypothesis',hypothesis)

    transformation = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemoveWhiteSpace(replace_by_space=True),
        jiwer.RemoveMultipleSpaces(),
        jiwer.ReduceToListOfListOfWords(word_delimiter=" ")
    ]) 

    error = jiwer.wer(
        ground_truth, 
        hypothesis, 
        truth_transform=transformation, 
        hypothesis_transform=transformation
    )   
    print('WER tính được là : ',error)