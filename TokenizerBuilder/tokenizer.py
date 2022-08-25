from tokenizers import ByteLevelBPETokenizer


class TrainBPETokenizer:
    def __init__(self):
        self.tokenizer = ByteLevelBPETokenizer()


    def train(self,paths,vocab_size,min_frequency,special_tokens):
        self.tokenizer.train(files=paths,vocab_size=vocab_size,min_frequency=min_frequency,special_tokens=special_tokens)
    
    def save_tokenizer(self,path):
        self.tokenizer.save_model(path)





