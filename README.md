# Find Missing Range

## 📌 Overview
This project provides a Python function `Find_missing_range` that identifies missing numbers in a sequence of frames.  
It returns:
- All missing ranges  
- The longest missing range  
- The total number of missing values  

---

## ⚙️ Function Explanation
1. Convert the input list of frames into a **set** for fast lookup.  
2. Iterate from `1` to the maximum frame number to find gaps.  
3. Store each gap as `[start, end]`.  
4. Count the total missing numbers.  
5. Identify the **longest missing range** (returns the first one if there’s a tie).  

---

## 📊 Time and Space Complexity
- **Time Complexity:**  
  - Set creation: `O(n)`  
  - Iteration up to max frame: `O(m)`  
  - **Overall:** `O(n + m)`  
  - (`n` = number of frames, `m` = maximum frame value)

- **Space Complexity:**  
  - Set storage: `O(n)`  
  - Gaps list (worst case): `O(m)`  
  - **Overall:** `O(n + m)`  

---

## 🖥️ Code
```python
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
```

---

## 📜 Basic Example
```python
frames = [1, 2, 5, 6, 10]
print(Find_missing_range(frames))
```
**Output:**
```python
{
  'gaps': [[3, 4], [7, 9]],
  'longest_gap': [7, 9],
  'missing_count': 5
}
```

---

## ✅ Test Cases

### 1) Empty input
```python
frames = []
Find_missing_range(frames)
```
**Expected:**
```python
{'gaps': [], 'longest_gap': None, 'missing_count': 0}
```

### 2) No missing numbers (continuous from 1)
```python
frames = [1, 2, 3, 4, 5]
```
**Expected:**
```python
{'gaps': [], 'longest_gap': None, 'missing_count': 0}
```

### 3) Missing at the start (from 1)
```python
frames = [5, 6, 7]
```
**Expected:**
```python
{'gaps': [[1, 4]], 'longest_gap': [1, 4], 'missing_count': 4}
```

### 4) Single missing in the middle
```python
frames = [1, 2, 4, 5]
```
**Expected:**
```python
{'gaps': [[3, 3]], 'longest_gap': [3, 3], 'missing_count': 1}
```

### 5) Multiple disjoint gaps
```python
frames = [1, 2, 5, 9, 10]
```
**Expected:**
```python
{'gaps': [[3, 4], [6, 8]], 'longest_gap': [6, 8], 'missing_count': 5}
```

### 6) Only a single frame far away
```python
frames = [10]
```
**Expected:**
```python
{'gaps': [[1, 9]], 'longest_gap': [1, 9], 'missing_count': 9}
```

### 7) Large max frame with sparse hits
```python
frames = [1, 1000]
```
**Expected:**
```python
{'gaps': [[2, 999]], 'longest_gap': [2, 999], 'missing_count': 998}
```

### 8) Tie in longest gaps (returns the first encountered)
```python
frames = [1, 5, 9]
```
- Missing ranges are `[2,4]` (length 3) and `[6,8]` (length 3).  
**Expected:**
```python
{'gaps': [[2, 4], [6, 8]], 'longest_gap': [2, 4], 'missing_count': 6}
```



---

## 👤 Author
- **Name:** Kadhim Riyadh  
- **Phone:** 07828744492  
