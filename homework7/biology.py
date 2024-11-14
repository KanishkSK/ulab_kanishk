import numpy as np
import aminoacidconverter

sequence = np.array(["AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"])
def counting_nucleotides(sequence):
     return ('A: ', int(np.char.count(sequence, 'A')), 'B: ', int(np.char.count(sequence, 'T')), 
            'C: ', int(np.char.count(sequence, 'C')), 'D: ', int(np.char.count(sequence, 'G')))


def checking_mutation(sequence1, sequence2): # checks whether mutation is missense, nonsense, or silent based on the input of two sequences.
    

    aas1 = aminoacidconverter.convert(aminoacidconverter.array_converter(sequence1)) # converts sequence 1 to amino acids
    aas2 = aminoacidconverter.convert(aminoacidconverter.array_converter(sequence2)) # converts sequence 2 to amino acids
    if sequence1 != sequence2 and len(aas1) > 0 and len(aas2) > 0 : #checks if there is a mutation in the first place.
        if len(aas1) != len(aas2): 
            #a nonsense mutation happens because it means that a mutation results in a premature STOP codon which will result in a shorter sequence
            return "Nonsense"
        
        elif np.array_equal(aas1, aas2):  
            # a silent mutation occurs when a mutation happens, but the amino acid sequence does not change. This is usually because of degeneracy, or the idea that multiple codons code for the same amino acid. 
            return "Silent"
        
        else: # missense occurs when there is a different amino acid in the mutated sequence, so
            # when aas1 != aas2 which should just be covered with else
            return "Missense"
    else: 
        return "No Mutation"



dna_matrix = [
    ["ATGC"], ["GCGC"], ["ATAT"],
    ["GCGT"], ["TATA"], ["CGCG"],
    ["TTTT"], ["GGGG"], ["CCCC"]
]

def gc_content(array): # the number of guanine and cytosine molecules indicates the stability of the DNA molecule. 
    percentages = []
    numofgs = 0
    numofcs = 0
    for sequence in array: 
        for i in range(len(sequence)): 
            if 'G' in sequence[i]:
                numofgs += 1/len(sequence[i]) * 100
            if 'C' in sequence[i]: 
                numofcs += 1/len(sequence[i]) * 100
        
        outputg = 'G: ' + str(numofgs ) + '%'
        outputc = 'C: ' + str(numofcs)  + '%'

        percentages.append([outputg, outputc])
        numofgs = 0
        numofcs = 0
    return percentages

"""
The percentage of C and G is important because cytosine and guanine has triple bonds while adesine and tyrosine has double bonds.
This means the more C and G present in a DNA molecule, the more stable it is because it has more bonds. 
"""