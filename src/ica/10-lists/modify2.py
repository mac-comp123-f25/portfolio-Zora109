
def remove_all(value, items):
    """
    Remove all occurrences of `value` from the list `items` in place.
    Preserves the order of the remaining elements.
    """
    # Simple approach using while + remove (readable; O(n*k) in worst case)
    while True:
        try:
            items.remove(value)
        except ValueError:
            break


if __name__ == "__main__":
    # Demo
    a = [1, 2, 3, 2, 4, 2, 5]
    print("Before:", a)
    remove_all(2, a)
    print("After: ", a)  # [1, 3, 4, 5]
