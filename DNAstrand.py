def verify(sequence):
    '''This code verifies if a sequence is a DNA or RNA'''
    # set the input sequence
    seq = set(sequence)
     
    # confirm if its elements is equal to the
    # set of valid DNA bases
    # Use a union method to ensure the sequence is
    # verified if does not contain all the bases
    if seq == {"A", "T", "C", "G"}.union(seq):
        return "DNA"
    elif seq == {"A", "U", "C", "G"}.union(seq):
        return "RNA"
    else:
        return "Invalid sequence"
 
 
seq1 = "ATGCAGCTGTGTTACGCGAT"
seq2 = "UGGCGGAUAAGCGCA"
seq3 = "TYHGGHHHHH"
 
print(seq1 + " is " + verify(seq1))
print(seq2 + " is " + verify(seq2))
print(seq3 + " is " + verify(seq3))

def verify(sequence):
    '''This code verifies if a sequence is a DNA or RNA'''
     
    # set the input sequence
    seq = set(sequence)
     
    # confirm if its elements is equal to 
    # the set of valid DNA bases
    # Use a union method to ensure the
    # sequence is verified if does not
    # contain all the bases
    if seq == {"A", "T", "C", "G"}.union(seq):
        return "DNA"
    elif seq == {"A", "U", "C", "G"}.union(seq):
        return "RNA"
    else:
        return "Invalid sequence"
 
 
def rev_comp_st(seq):
    '''This function returns a reverse complement 
    of a DNA or RNA strand'''
    verified = verify(seq)
    if verified == "DNA":
       
        # complement strand
        seq = seq.replace("A", "t").replace(
            "C", "g").replace("T", "a").replace("G", "c")
        seq = seq.upper()
         
        # reverse strand
        seq = seq[::-1]
        return seq
 
    elif verified == "RNA":
       
        # complement strand
        seq = seq.replace("A", "u").replace(
            "C", "g").replace("U", "a").replace("G", "c")
        seq = seq.upper()
         
        # reverse strand
        seq = seq[::-1]
        return seq
    else:
        return "Invalid sequence"
 
 
# test variables
seq1 = "ATGCAGCTGTGTTACGCGAT"
seq2 = "UGGCGGAUAAGCGCA"
seq3 = "TYHGGHHHHH"
 
print("The reverse complementary strand of " +
      seq1 + " is " + rev_comp_st(seq1))
print("The reverse complementary strand of " +
      seq2 + " is " + rev_comp_st(seq2))
print("The reverse complementary strand of " +
      seq3 + " is " + rev_comp_st(seq3))