from seq_utils.seq_utils import *
from boyer_moore.boyer_moore import *
from index.index import *
from naive.naive import *
from subseq_index.subseq_index import *

# t = read_genome("chr1.GRCh38.excerpt.fasta")

# p = "GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG"

# Question 1
# occurrences, alignments_num, comparisons_num = hw2.naive_with_counts(p, t)
# print(alignments_num)

# Question 2
# print(comparisons_num)

# Question 3
# p_bm = hw2.BoyerMoore(p)
# occurrences, alignments_num, comparisons_num = hw2.boyer_moore_with_counts(p, p_bm, t)
# print(alignments_num)

# Question 4
# def approximate_match(p, index, t, n):
#     """Finds all approximate occurrences of p within t with up to n mismatches."""
#     segment_length = int(round(len(p) / (n + 1)))
#     all_matches = set()
#     for i in range(n + 1):
#         start = i * segment_length
#         end = min((i + 1) * segment_length, len(p))
#         # Use index to search for exact matches
#         matches = index.query(p[start:end])
#         # Extend matching segments to see if whole p matches
#         for m in matches:
#             if m < start or m - start + len(p) > len(t):
#                 continue
#             mismatches = 0
#             for j in range(0, start):
#                 if not p[j] == t[m - start + j]:
#                     mismatches += 1
#                     if mismatches > n:
#                         break
#             for j in range(end, len(p)):
#                 if not p[j] == t[m - start + j]:
#                     mismatches += 1
#                     if mismatches > n:
#                         break
#             if mismatches <= n:
#                 all_matches.add(m - start)
#     return list(all_matches)


# p = "GGCGCGGTGGCTCACGCCTGTAAT"
# index = Index(t, 8)
# matches = approximate_match(p, index, t, 2)
# print(len(matches))

# Question 5
# m, h = approximate_match(p, index, t, 2)
# print(h)

# Question 6
# def approximate_match_subseq(p, index, t, n):
#     """Finds all approximate occurrences of p within t with up to n mismatches."""
#     all_matches = set()
#     hits = 0
#     for i in range(n + 1):
#         # Use index to search for exact matches
#         matches = index.query(p)
#         hits += len(matches)
#     return list(all_matches), hits


# p = "GGCGCGGTGGCTCACGCCTGTAAT"
# index = SubseqIndex(t, 8, 3)
# matches, hits = approximate_match_subseq(p, index, t, 2)
# print(hits)


