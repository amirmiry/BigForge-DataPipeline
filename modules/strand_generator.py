def strand_Generate(Dict):
    forward = Dict["Sequence"]
    complement = make_Complement(foeward)
    reverse = complement[ : : -1]
    return {"forward":forwrad, "reverse_Complement": reverse}
    


    
    
def make_Complement(forward):
    Pa ={"A":"T","T":"A","C":"G","G":"C"}
    for i in forward:
        Complement = "".joind(Pa[i])
    return Complement
    
