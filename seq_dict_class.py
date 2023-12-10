from sequence_class import Seq

class SeqDict:
    def __init__(self):
        self.length = 0
        self.dictionary = dict()
    
    def add_entry(self, Seq):
        self.dictionary.update({Seq.get_seq_number(): Seq.get_str()})
        self.length += 1
    
    def get_entry(self, key):
        return self.dictionary[key]

    def get_length(self):
        return len(self.dictionary)