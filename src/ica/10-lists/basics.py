from typing import List, Iterable

def every_other(items: Iterable) -> list:
    """
    Return a new list containing every other element from items,
    starting with index 0.
    Examples:
        every_other([0,1,2,3,4]) -> [0, 2, 4]
    """
    return list(items)[::2]


def sum_positive(nums: Iterable[float]) -> float:
    """
    Return the sum of the positive numbers in nums (strictly > 0).
    Zeros and negatives are ignored.
    """
    total = 0
    for x in nums:
        if x > 0:
            total += x
    return total


# --- quick self-tests (you can delete below this line before submitting) ---
if __name__ == "__main__":
    print(every_other([1, 2, 3, 4, 5, 6]))       # [1, 3, 5]
    print(every_other("abcdefg"))                # ['a', 'c', 'e', 'g']
    print(sum_positive([3, -2, 0, 4.5, -7, 1]))  # 8.5
