def parser_validator(fasta :str):
        if fasta !="" and isinstance(fasta ,str) and fasta[0] == "<":
            return Clean(fasta)
         
        else:
            raise ValueError