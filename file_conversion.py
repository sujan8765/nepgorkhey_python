import sys
filename = sys.argv[-1]
from Bio import SeqIO
from Bio.Alphabet import generic_dna
if filename[-4:]==".nex":
	SeqIO.convert(filename, "nexus", filename[:-4]+".fas", "fasta", generic_dna)
	print ("file converted from nexus to fasta")
if filename[-4:]==".fas":
	SeqIO.convert(filename, "fasta", filename[:-4]+".nex", "nexus", generic_dna)
	print ("file converted from fasta to nexus")