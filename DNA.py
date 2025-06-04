def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in reversed(dna))

dna_sequence = "AAGTC"
reversed_complement = reverse_complement(dna_sequence)
print(f"Original DNA sequence: {dna_sequence}")
print(f"Reverse complement: {reversed_complement}")