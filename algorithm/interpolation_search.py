"""
Interpolation Search
Complexity O(log log n) if list respects input, else O(n)
Input: list - sorted, uniformly distributed
       val - element to search for
Output: index of val in list or -1
"""

def InterpolationSearch(lys: list, val) -> int:
    low = 0
    high = len(lys) - 1

    while low <= high and lys[low] <= val <= lys[high]:
        index = low + int(
            ((high - low) / (lys[high] - lys[low])) * (val - lys[low])
        )

        if lys[index] == val:
            return index

        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1

    return -1
