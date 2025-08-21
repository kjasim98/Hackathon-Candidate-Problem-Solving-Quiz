def Find_missing_range(frames):
    s = set(frames)
    if not s:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}

    max_f = max(s)
    gaps = []
    i = 1
    while i <= max_f:
        if i not in s:
            start = i
            while i <= max_f and i not in s:
                i += 1
            end = i - 1
            gaps.append([start, end])  
        else:
            i += 1

    missing_count = sum(end - start + 1 for start, end in gaps)

    # Find the longest missing range
    # Assumption: If there are multiple ranges with the same maximum length,
    # we will return the first one encountered.
    longest_gap = None
    longest_len = 0
    for start, end in gaps:
        length = end - start + 1
        if length > longest_len:
            longest_len = length
            longest_gap = [start, end]

    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }


# Run the tests
run_tests()
