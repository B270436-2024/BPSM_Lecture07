#!/usr/bin/python3
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
at_content = (my_dna.count('A') + my_dna.count('T')) / len(my_dna)
print("A+T content is",str(int(100*at_content)),"percent")

print("The complement sequence is", my_dna.replace('A', 't').replace('T','a').replace('G','c').replace('C','g').upper())

site = "GAATTC"
print("Lengths of",site,"cleaved fragments are",my_dna.find(site) + 1,"and",len(my_dna) -(my_dna.find(site)+1),"bases")

my_dna2 ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna2[0:63]
exon2 = my_dna2[90:]
print("### Exons joined ###\n" + exon1 + exon2)

coding_length = len(exon1 + exon2)
total_length = len(my_dna2)
print("### Coding percentage (rounded) ###\n" + str(int((coding_length / total_length) * 100)))

intron = my_dna[63:90]
print("### Exon intron exon ###\n" + exon1 + intron.lower() + exon2)
