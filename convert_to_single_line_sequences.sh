ls *.fasta >> nucleotide.txt
cat nucleotide.txt | while read x
do	
	x2=${x%.*}
	awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' < $x > $x2"_single_line.fas"
	echo "$(tail -n +2 "$x2"_single_line.fas)" > $x2"_single_line.fas"
done

rm -r nucleotide.txt

ls *.faa >> amino_acid.txt
cat amino_acid.txt | while read x
do	
	x2=${x%.*}
	awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' < $x > $x2"_single_line.faa"
	echo "$(tail -n +2 "$x2"_single_line.faa)" > $x2"_single_line.faa"
done

rm -r amino_acid.txt