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
    a_count = dna.count('A')
    c_count = dna.count('C')
    g_count = dna.count('G')
    t_count = dna.count('T')
    num_of_nucleotides = f"""[A - {a_count}, C - {c_count}, G - {g_count},\
 T - {t_count}]"""
    plotter(a_count, c_count, g_count, t_count)
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
dna_words = {}
dna_temp = ''

with open("./dna.fasta") as dna_input:
    for line in dna_input:
        if line.startswith('>'):
            if dna_temp != '':
                dna_words[dna_desc] = dna_temp
                dna_temp = ''
            dna_desc = line.strip('\r\n')[1:]
        else:
            dna_temp += line.strip('\r\n')
    dna_words[dna_desc] = dna_temp

for dna in dna_words.items():
    key, val = dna
    with open('./nucleotides_count.txt', 'a') as nc:
        nc.write(f'{key}: {count_nucleotides(val)}\n')
    with open('./rna_transcripted.txt', 'a') as rna:
        curr_rna = translate_from_dna_to_rna(val)
        rna.write(f'{key}: {curr_rna}\n')
    with open('./proteins_transcripted.txt', 'a') as prots:
        prots.write(f'{key}: {translate_rna_to_protein(curr_rna)}\n')
