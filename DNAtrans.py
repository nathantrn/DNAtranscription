from sys import argv
#function creates dictionary
def CodonDict(codontable):
	CodonMatrix = []
	for line in open(codontable, "r"):
		#condition ensures that empty lines are skipped
        	if ("A" in line or "C" in line or "G" in line or "T" in line):
                	elements = line.strip().split()
                	CodonMatrix.append(elements)

	CodonLibrary = {}
	for codon in CodonMatrix:
        	i = 0
        	while i < 64:
			#goes through each row of the matrix and sets the first column entry equal to its second column counterpart
                	CodonLibrary[CodonMatrix[i][0]] = CodonMatrix[i][1]
                	i += 1
	#returns dictionary to be used
	return CodonLibrary

#function creates protein string
#needs input of starting index(i), the compensation index needed to ensure there are perfect reading frame, the nucleotide sequence, and the dictionary 
def proteinconvert(i, s, string, CodonDict):
	protein = ""
	#(i+2 < len(string) - s) in order to ensure that checked index is always within the string's range
	while i+2 < (len(string) - s):
		#sets codon equal to the next three nucleotides
		codon = string[i] + string[i+1] + string[i+2]
		if codon in CodonDict.keys():
			#matches Codon with its protein and adds protein to protein string 
			amino = CodonDict[codon]
			protein = protein + amino
		#goes to next frame
		i+=3
	#reads protein string for start and stop sequences
	k = 0
	#checks every character of protein string
	while k < len(protein):
		#if the amino acid is a indicates start then save that index as begin
        	if (protein[k] == "M"):
                	begin = k
                	n = k
			#continue to check next characters after start codon to look for a stop codon
                	while n < len(protein):
                        	if (protein[n] == "-"):
					#when stop is found record index as end
					#n+1 in order to print "-" at end of string
                                	end = n + 1
                                	break;
                        	else:
                                	n += 1
			#print protein from the begin index to the end index
                	print(protein[begin:end])
		#after printing protein begin to end, go back to look for the next start sequence
        	k += 1

#creates dictionary from argument 2
CDict = CodonDict(argv[2])
string = ""
#converts genome sequence to nucleotide string
for line in open(argv[1], "r"):
	#skip line with ">"
        if ">" in line:
                string = string
        else:
                string = string + line
#gets rid of returns
string = string.replace('\n',"")
#changes string to uppercase
string = string.upper()

proteinconvert(0, 0, string, CDict)
proteinconvert(1, 2, string, CDict)
proteinconvert(2, 1, string, CDict)

#reverstring portion
rstring = string[::-1]
revSTRING = ""
#creates a complement string from the reversed original string
for char in rstring:
	if (char == "A"):
		revSTRING = revSTRING + "T"
	if (char == "T"):
		revSTRING = revSTRING + "A"
	if (char == "G"):
		revSTRING = revSTRING + "C"
	if (char == "C"):
		revSTRING = revSTRING + "G"


proteinconvert(0, 0, revSTRING, CDict)
proteinconvert(1, 2, revSTRING, CDict)
proteinconvert(2, 1, revSTRING, CDict)


