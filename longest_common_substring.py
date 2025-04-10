def read_fasta(filename):
    sequences = []
    with open(filename, 'r') as file:
        seq = ''
        for line in file:
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line.strip()
        if seq:
            sequences.append(seq)
    return sequences

def all_longest_common_substring(strings):
    shortest = min(strings, key=len)
    length = len(shortest)
    longest_common = set()
    max_len = 0

    for l in range(length, 0, -1):
        for i in range(length - l + 1):
            candidate = shortest[i:i + l]
            if all(candidate in s for s in strings):
                if l > max_len:
                    longest_common = {candidate}
                    max_len = l
                elif l == max_len:
                    longest_common.add(candidate)
        if max_len > 0:
            break
    return longest_common
                
if __name__== "__main__":
    dna_strings = read_fasta("input.txt")
    results = all_longest_common_substring(dna_strings)
    for res in sorted(results):
        print(res)
