filename = raw_input("Please input the complete genome name with filename and extension: ")
genome = open(filename)
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
print "total number of contigs are:", contig_number 
print "total genome length is:", count
print "The length of longest contig is:", longest

genome = open(filename)
half_genome = float(count/2)
N50_value = 0

for items in contigs_length:
	N50_value = N50_value + items
	if ( N50_value > half_genome ):
		print "The N50 value is:", items
		break
	else:
		continue
