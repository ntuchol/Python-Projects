print("\t\t\t\tMultiplication Tables\n")

for i in range(1,13):
  print(i, end = "\t")
print()
print("_____________________________")

for j in range(1, 13):
  for k in range(1, 13):
    print(j*k, end = "\t")
  print("\n")
