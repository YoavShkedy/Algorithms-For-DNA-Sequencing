def editDistance(p, t):
    # Create distance matrix
    D = [[i if j == 0 else 0 for j in range(len(t)+1)] for i in range(len(p)+1)]
    # Fill in the rest of the matrix
    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            dist_hor = D[i][j-1] + 1
            dist_ver = D[i-1][j] + 1
            if p[i-1] == t[j-1]:
                dist_diag = D[i-1][j-1]
            else:
                dist_diag = D[i-1][j-1] + 1
            D[i][j] = min(dist_hor, dist_ver, dist_diag)
    # Edit distance is the minimum value in the bottom row of the matrix
    return min(D[-1])


def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match


def overlap_all_pairs(reads, k):
    olaps = []
    graph = {}
    d = {}
    for read in reads:
        for i in range(len(read)-k+1):
            kmer = read[i:i+k]
            if d.get(kmer) is None:
                d[kmer] = set()
            d.get(kmer).add(read)

    for a in reads:
        if d.get(a[-k:]) is None:
            continue
        for b in d[a[-k:]]:
            olen = overlap(a, b, k)
            if olen == len(a):
                continue
            if olen > 0:
                olaps.append((a, b))
                graph[a] = b
    return olaps, graph
