import argparse
import torch 

def get_args():
    parser = argparse.ArgumentParser(description="Get the argument")

    #prepare_data
    parser.add_argument("--data_dir",type=str,default="data")
    parser.add_argument("--extract_data",action="store_false")

    parser.add_argument("--scenario",type=str,default="prepare_data")












    args = parser.parse_args()
    args.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return args