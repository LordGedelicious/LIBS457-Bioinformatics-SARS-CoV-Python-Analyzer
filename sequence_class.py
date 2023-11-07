class Seq:
    def __init__(self, seq_num, seq_str):
        self.seq_num = seq_num
        self.seq_str = seq_str
    
    def __str__(self):
        return self.seq_str
    
    def __len__(self):
        return len(self.seq_str)
    
    def get_seq_num(self):
        return self.seq_num