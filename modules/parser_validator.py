def parser_validator(fasta :str):
        if fasta !="" and isinstance(fasta ,str) and fasta[0] == "<":
            return Clean(fasta)
         
        else:
            raise ValueError
        


def Clean(fasta):
    lst = fasta.split("\n")
    id_list = lst[0]
    Sequence_list= lst[1]
    ID_clean = clean_id(id_list)
    Sequence_clean = clean_sequence(Sequence_list)
    Dict = {"id": ID_clean , "sequence": Sequence_clean}
    return Dict
