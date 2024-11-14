import numpy as np


# RNA codon table which I stole online because it's a lot to write out
# essentially just assosiates short rna sequences that are three bases long (these are called codons) with their
# coresponding amino acids
rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
           "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
           "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
           "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
           "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
           "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
           "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
           "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }



def array_converter(sequence):
    arr = []  
    for i in range(0, len(sequence), 3):
        arr.append(sequence[i:i+3])  
    arr = np.array(arr)  
    print("Nucleotide Sequence: ", arr)
    return arr

def convert(rna): 
    protein_string = np.array([])

    for j in range(len(rna)):
        if rna[0] == 'AUG': # indicates START codon
            for i in range(0,len(rna)):
                if rna_codon.get(rna[i]) == "STOP" :
                    print ("Protein String: ", protein_string)
                    return protein_string
                protein_string = np.append(protein_string, rna_codon.get(rna[i]))
                
            #print ("Protein String: ", protein_string)
            return protein_string
        
"""if rna_codon.get(rna[i:i+3:1]) == "STOP" :
                    return protein_string"""

