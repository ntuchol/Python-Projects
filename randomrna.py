import random

def generate_random_rna(length):
    """Generates a random RNA sequence of specified length.

    Args:
        length: An integer representing the desired length of the RNA sequence.

    Returns:
        A string representing the random RNA sequence.
    """
    rna_nucleotides = "AUCG"
    return ''.join(random.choice(rna_nucleotides) for _ in range(length))

# Example usage:
rna_sequence = generate_random_rna(20)
print(rna_sequence)