from seq_utils.seq_utils import reverse_complement


def naive(p, t):
    """Finds offsets where pattern p occurs within text t"""
    return naive_mm(p, t, 0)


def naive_with_rc(p, t):
    """Finds offsets where pattern p and its reverse occur within text t"""
    p_rc = reverse_complement(p)
    if p_rc == p:   # In case p is equal to its reverse complement
        return naive(p, t)  # p equals to its rc, execute naive
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # Loop over alignments
        match = True
        match_rc = True
        for j in range(len(p)):  # Loop over characters
            if not match and not match_rc:
                break
            if match:
                if t[i+j] != p[j]:  # Compare characters of p
                    match = False
            if match_rc:
                if t[i+j] != p_rc[j]:   # Compare characters of rc of p
                    match_rc = False
        if match or match_rc:
            occurrences.append(i)  # All chars of one or both matched - record
    return occurrences


def naive_2mm(p, t):
    """Finds offsets where pattern p occurs within
         text t. Allows up to m=2 mismatches per occurrence."""
    return naive_mm(p, t, 2)


def naive_mm(p, t, m):
    """Finds offsets where pattern p occurs within
        text t. Allows up to m mismatches per occurrence."""
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        mistakes = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                if mistakes == m:
                    match = False
                    break
                mistakes += 1
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def naive_with_counts(p, t):
    """Finds offsets where pattern p occurs within text t. Counts and returns
     (a) occurrences of p within t
     (b) the number of alignments tried
     (c) the number of character comparisons performed."""
    occurrences = []
    alignments = 0
    comparisons = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        alignments += 1
        match = True
        for j in range(len(p)):  # loop over characters
            comparisons += 1
            if t[i + j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, alignments, comparisons
