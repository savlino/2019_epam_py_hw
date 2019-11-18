# dna homework
import matplotlib.pyplot as plt

dna_to_rna_dict = {"A": "U", "T": "A", "G": "C", "C": "G"}

codons_dict = {}


def make_codons_dict():
    with open("./rna_codon_table.txt") as codons:
        for line in codons:
            if "Stop" not in line:
                pairs = line.strip('\n').split('      ')
            else:
                pairs = line.strip('\n').split('   ')
                del pairs[2::2]
            for pair in pairs:
                k, v = pair.strip().split(' ')
                codons_dict[k] = v


def count_nucleotides(dna):
    # accepts stripped DNA string and returns nucleotides chart as string
    A_count = dna.count('A')
    C_count = dna.count('C')
    G_count = dna.count('G')
    T_count = dna.count('T')
    num_of_nucleotides = f"""[A - {A_count}, C - {C_count}, G - {G_count},\
 T - {T_count}]"""
    plotter(A_count, C_count, G_count, T_count)
    return num_of_nucleotides


def translate_from_dna_to_rna(dna):
    # accepts stripped DNA string and returns RNA string
    rna = ''
    for k in dna:
        rna += dna_to_rna_dict[k]
    return rna


def translate_rna_to_protein(rna):
    # accepts stripped RNA string and returnd protein sequence
    protein = ''
    i = 0
    while i <= len(rna):
        cur_sect = rna[i:i + 3]
        if len(cur_sect) < 3:
            break
        protein += codons_dict[cur_sect]
        i += 3
    return protein


def plotter(a, b, c, d):
    x = [0, 1, 2, 3]
    values = [a, b, c, d]
    plt.bar(x, values)
    plt.xticks(x, ['A', 'C', 'G', 'T'])
    plt.show()


make_codons_dict()
DNA_words = {}
DNA_temp = ''

with open("./dna.fasta") as DNA_input:
    for line in DNA_input:
        if line.startswith('>'):
            if DNA_temp != '':
                DNA_words[dna_desc] = DNA_temp
                DNA_temp = ''
            dna_desc = line.strip('\r\n')[1:]
        else:
            DNA_temp += line.strip('\r\n')
    DNA_words[dna_desc] = DNA_temp

for DNA in DNA_words.items():
    key, val = DNA
    with open('./nucleotides_count.txt', 'a') as nc:
        nc.write(f'{key}: {count_nucleotides(val)}\n')
    with open('./rna_transcripted.txt', 'a') as rna:
        curr_rna = translate_from_dna_to_rna(val)
        rna.write(f'{key}: {curr_rna}\n')
    with open('./proteins_transcripted.txt', 'a') as prots:
        prots.write(f'{key}: {translate_rna_to_protein(curr_rna)}\n')
