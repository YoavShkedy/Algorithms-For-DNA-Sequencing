from seq_utils.seq_utils import *
from naive.naive import *

lambda_virus_genome = read_genome("lambda_virus.fa")

occurrences1 = naive_with_rc("AGGT", lambda_virus_genome)
print(len(occurrences1), "\n")

occurrences2 = naive_with_rc("TTAA", lambda_virus_genome)
print(len(occurrences2), "\n")

occurrences3 = naive_with_rc("ACTAAGT", lambda_virus_genome)
print(min(occurrences3), "\n")

occurrences4 = naive_with_rc("AGTCGA", lambda_virus_genome)
print(min(occurrences4), "\n")

occurrences5 = naive_2mm("TTCAAGCC", lambda_virus_genome)
print(len(occurrences5), "\n")

occurrences6 = naive_2mm("AGGAGGTT", lambda_virus_genome)
print(min(occurrences6), "\n")

seqs, quals = read_fastq("ERR037900_1.first1000.fastq")
max_seq_len = len(max(seqs))
cycles_list = [0 for _ in range(max_seq_len)]
for i in range(len(seqs)):
    for offset in range(len(seqs[i])):
        cycles_list[offset] += phred33_to_q(quals[i][offset])
print(cycles_list.index(min(cycles_list)))
