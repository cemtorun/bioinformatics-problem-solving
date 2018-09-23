with open("Monoisotopic Mass Table.txt") as file:
    isotopic_mass_table = file.read()

isotopic_mass_index = {}
total_protein_mass = 0

isotopic_mass_table = isotopic_mass_table.split()

for counter, element in enumerate(isotopic_mass_table[0::1]):
    if element.isalpha():
        isotopic_mass_index[element] = isotopic_mass_table[counter + 1]

with open("rosalind_prtm.txt") as file:
    protein_primary_structure = file.read()

protein_primary_structure.split()

for amino_acid in protein_primary_structure:
    if amino_acid != "\n":
        total_protein_mass += float(isotopic_mass_index[amino_acid])


print(round(total_protein_mass, 3))
