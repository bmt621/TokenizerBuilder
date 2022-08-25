'''
                                 TRAINING TOKENIZER
from pathlib import Path
from tokenizer import *

path_to_txt_files = 'path/to/txtfiles'

paths = [str(x) for x in Path(path_to_txt_files).glob('*.txt')]

bpetokenizer = TrainBPETokenizer()
special_tokens = ['<s>','</s>','<pad>','<unk>']

bpetokenizer.train(paths,vocab_size = 30_000,min_frequency=2,special_tokens=special_tokens)
path_to_tokenizer = 'path/to/tokenizer

bpetokenizer.save_tokenizer(path_to_tokenizer)

                                  LOADING TOKENIZER

from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained(path_to_tokenizer)


'''