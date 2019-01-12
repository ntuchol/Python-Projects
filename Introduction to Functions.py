#Problem 1
#The following function converts between degrees Celsius and Fahrenheit

def convert_to_Celsius(Fahrenheit):
  Celsius = (Fahrenheit - 32)*5/9
  return Celsius

print("32 F in C:", convert_to_Celsius(32))
print("212 F in C:", convert_to_Celsius(212))


# Code for Problem 2 goes here.
def sum_of_multiples(multiple, lower, upper):
    result = 0
    for i in range(lower, upper):
        if i%multiple == 0:
            result += i
    return result

print(sum_of_multiples(3, 1, 31))

#Code for Problem 3 goes here.
def calc_mol_weight(protseq):
    amino_weights = {'A':89.09,'R':174.20,'N':132.12,'D':133.10,
                     'C':121.15,'Q':146.15,'E':147.13,'G':75.07,
                     'H':155.16,'I':131.17,'L':131.17,'K':146.19,
                     'M':149.21,'F':165.19,'P':115.13,'S':105.09,
                     'T':119.12,'W':204.23,'Y':181.19,'V':117.15}
    weight = 0
    for aa in protseq:
        if aa in amino_weights:
            weight += amino_weights[aa]
    return weight

# Variables for testing that the function works properly.
protseq1 = "AGAHHCTPL" # weight = 1050.14
protseq2 = "HQWRSSXAD" # weight = 1112.11

# Run the function on protseq1 and protseq2.
print(calc_mol_weight(protseq1))
print(calc_mol_weight(protseq2))

#Problem 4 
# this doesn't work because of rounding errors
print("Incorrect implementation of test:")
if calc_mol_weight(protseq1)==1050.14:
    print("result correct for protseq1")
else:
    print("result incorrect for protseq1")
if calc_mol_weight(protseq2)==1112.11:
    print("result correct for protseq1")
else:
    print("result incorrect for protseq2")

# we need to test whether they fall into a given small range of values:
print("Correct implementation of test:")
if abs(calc_mol_weight(protseq1)-1050.14) < 0.00001:
    print("result correct for protseq1")
else:
    print("result incorrect for protseq1")
if abs(calc_mol_weight(protseq2)-1112.11) < 0.00001:
    print("result correct for protseq1")
else:
    print("result incorrect for protseq2")  
