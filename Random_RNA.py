import random

def generate_random_rna(length):
    
    rna_nucleotides = "AUCG"
    return ''.join(random.choice(rna_nucleotides) for _ in range(length))

rna_sequence = generate_random_rna(20)
print(rna_sequence)
