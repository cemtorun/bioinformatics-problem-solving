# Finding the same interval of DNA in the genomes of two different
# organisms (often taken from different species) is highly suggestive
#  that the interval has the same function in both organisms.

# We define a motif as such a commonly shared interval of DNA. A common task
# in molecular biology is to search an organism's genome for a known motif.

with open("rosalind_subs.txt") as file:
    dna_sequence_motif = file.read()

DNA_sequence = dna_sequence_motif.split()[0]
motif = dna_sequence_motif.split()[1]

motif_list = []

for counter, nucleotide in enumerate(DNA_sequence):
    if DNA_sequence[counter:counter + len(motif)] == motif:
        motif_list.append(counter + 1)


for i in motif_list:
    print(i, end=" ")




