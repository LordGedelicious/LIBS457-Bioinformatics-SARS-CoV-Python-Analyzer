class Seq:
    def __init__(self, seq_num, seq_str):
        self.seq_num = seq_num
        self.seq_str = seq_str
    
    def get_str(self):
        return self.seq_str
    
    def get_len(self):
        return len(self.seq_str)
    
    def get_seq_num(self):
        return self.seq_num
    
    def print_fasta_format(self):
        print(">Seq{}".format(self.seq_num))
        print(self.seq_str)
        print()
    
    def return_fasta_format(self):
        return ">Seq{}\n{}\n".format(self.seq_num, self.seq_str)