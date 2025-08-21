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

def run_tests():
    test_cases = [
        # 1. Empty input
        ([], {"gaps": [], "longest_gap": None, "missing_count": 0}),

        # 2. Continuous sequence (no gaps)
        ([1, 2, 3, 4, 5], {"gaps": [], "longest_gap": None, "missing_count": 0}),

        # 3. Single gap in the middle
        ([1, 2, 5, 6], {"gaps": [[3, 4]], "longest_gap": [3, 4], "missing_count": 2}),

        # 4. Missing numbers at the beginning
        ([3, 4, 5], {"gaps": [[1, 2]], "longest_gap": [1, 2], "missing_count": 2}),

        # 5. Missing numbers at the end
        ([1, 2, 3], {"gaps": [], "longest_gap": None, "missing_count": 0}),  # since max=3

        # 6. Multiple small gaps
        ([1, 3, 5, 7], {"gaps": [[2, 2], [4, 4], [6, 6]], "longest_gap": [2, 2], "missing_count": 3}),

        # 7. One long gap
        ([1, 10], {"gaps": [[2, 9]], "longest_gap": [2, 9], "missing_count": 8}),

        # 8. Large range with multiple gaps
        ([1, 2, 5, 9, 10], {"gaps": [[3, 4], [6, 8]], "longest_gap": [6, 8], "missing_count": 5}),

        # 9. Single element
        ([5], {"gaps": [[1, 4]], "longest_gap": [1, 4], "missing_count": 4}),

        # 10. Mixed scattered numbers
        ([2, 4, 7, 10], {"gaps": [[1, 1], [3, 3], [5, 6], [8, 9]], "longest_gap": [5, 6], "missing_count": 6}),
    ]

    for i, (frames, expected) in enumerate(test_cases, 1):
        result = Find_missing_range(frames)
        if result == expected:
            print(f"Test case {i}: PASS")
        else:
            print(f"Test case {i}: FAIL")
            print(f"  Input: {frames}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")


# Run the tests
run_tests()