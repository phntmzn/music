def transpose(pcset, n):
    return sorted((p + n) % 12 for p in pcset)

def invert(pcset):
    return sorted((12 - p) % 12 for p in pcset)

def invert_and_transpose(pcset, n):
    return sorted((n - p) % 12 for p in pcset)

def find_identity_functions(pcset):
    identities = []

    # Transpositional identities: Tn(pcset) == pcset
    for n in range(12):
        if sorted(transpose(pcset, n)) == sorted(pcset):
            identities.append(f"T{n}")

    # Inversional identities: I(n)(pcset) == pcset
    for n in range(12):
        inv_trans = invert_and_transpose(pcset, n)
        if sorted(inv_trans) == sorted(pcset):
            identities.append(f"I{n}")

    return identities

if __name__ == "__main__":
    # Symmetric tritone chord (e.g., C, F#)
    pcs = [0, 6]
    print("Pitch Class Set:", pcs)
    print("Identity Functions:", find_identity_functions(pcs))

    # C major chord (not symmetric)
    pcs = [0, 4, 7]
    print("\nPitch Class Set:", pcs)
    print("Identity Functions:", find_identity_functions(pcs))
