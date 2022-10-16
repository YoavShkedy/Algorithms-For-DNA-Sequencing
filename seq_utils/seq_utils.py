def read_genome(filename):
    """Parses a DNA reference genome from a FASTA file"""
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def read_fastq(filename):
    """Parses the read and quality strings from
        a FASTQ file containing sequencing reads"""
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def reverse_complement(s):
    """Takes a DNA string s and returns its reverse complement"""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t


def phred33_to_q(qual):
    """Convert Phred33 encoded value to quality score"""
    return ord(qual) - 33


def create_hist(qualityStrings):
    """Create a histogram of quality scores"""
    hist = [0]*50
    for read in qualityStrings:
        for phred in read:
            q = phred33_to_q(phred)
            hist[q] += 1
    return hist


def plot_hist(hist):
    """Plot a histogram hist"""
    import matplotlib.pyplot as plt
    plt.plot(range(len(hist)), hist)
    plt.show()
