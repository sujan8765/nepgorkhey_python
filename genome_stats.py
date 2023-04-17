# provide an input file as: python genome_stats.py 1.fastq 2.fastq genome.fasta
# the fastq file should be unzipped and not in .gz format. 
# if zipped: unzip using respective unzipping commands. 
# the assembled genomes should have continuous sequence and not in sequences separated in individual lines
# for example: the contigs in the genome.fasta should be arranged as follows:
# >genome_contig_1.fasta
# ATCGAATGAAT
# >genome_contig_2.fasta
# ATTNACATTAGC

# but not as the following format
# >genome_contig_1.fasta
# ATCGA
# ATGAAT
# >genome_contig_2.fasta
# ATTNAC
# ATTAGC
import sys
forward = sys.argv[1]
reverse = sys.argv[2]
genome_file = sys.argv[3]

#for forward fastq file
with open(forward) as fwd:
        forward_read=fwd.readlines()	# splitting the lines
		# identify total number of reads for counter 
        fwd_read_lines = len(forward_read)	
        fwd_read_counter = int(fwd_read_lines/4)
        count = 1
        # extracting lines and their length
        line_count = 1 
        fwd_read_length = 0
        while count < fwd_read_counter:
        	fwd_read_length = fwd_read_length + len(forward_read[line_count]) - 1
        	line_count = line_count + 4
        	count = count + 1

# for reverse fastq file
with open(reverse) as rev:
        reverse_read=rev.readlines()	# splitting the lines
		# identify total number of reads for counter 
        rev_read_lines = len(reverse_read)	
        rev_read_counter = int(rev_read_lines/4)
        count = 1
        # extracting lines and their length
        line_count = 1 
        rev_read_length = 0
        while count < rev_read_counter:
        	rev_read_length = rev_read_length + len(reverse_read[line_count]) - 1
        	line_count = line_count + 4
        	count = count + 1

print ("\n")
print (genome_file)
print ("Total number of forward reads: ", fwd_read_counter)
print ("Total number of reverse reads: ", rev_read_counter)
print ("Forward read length: ", fwd_read_length)
print ("Reverse read length: ", rev_read_length)

# to calculate the genome.fasta assembled statistics. 
genome = open(genome_file)
count = 0
longest = 1
id_list = []
contigs_length=[]
for lines in genome:
	if lines[0]!= '>':
		actual_length = len(lines) - 1
		contigs_length.append(actual_length)
		count = count + actual_length
		if ( actual_length >= longest ):
			longest = actual_length
		else:
			longest = longest
	if lines[0] == '>':
		id_list.append(lines)
contig_number = len(id_list)
contigs_length = sorted(contigs_length, key=int, reverse=True)

print ("total number of contigs are:", contig_number)
print ("total genome length is:", count)
print ("The length of longest contig is:", longest)

coverage = (fwd_read_length + rev_read_length)/count

print ("The sequencing coverage is: ", coverage)

half_genome = float(count/2)
N50_value = 0
for items in contigs_length:
	N50_value = N50_value + items
	if ( N50_value > half_genome ):
		print ("The N50 value is:", items)
		break
	else:
		continue

