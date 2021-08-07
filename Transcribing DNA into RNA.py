L = open("rosalind_rna.txt", "rt")

M = open("out.txt", "wt")

for chr in L:
	
	M.write(chr.replace('T', 'U'))
