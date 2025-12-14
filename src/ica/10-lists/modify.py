
def change_start(value, items):
    """Mutate the list in place: set index 0 to value."""
    if not items:
        raise IndexError("Empty list has no index 0.")
    items[0] = value

if __name__ == "__main__":
    # Demo for change_start
    t_list = ['a', 'b', 'c', 'd', 'e', 'f']
    change_start('X', t_list)
    print(t_list)  # ['X', 'b', 'c', 'd', 'e', 'f']

    # Quick list-methods demo (safe examples only)
    list1 = [5, 6, 7]
    list2 = [4, 3, 2, 1]
    list1.append(8)
    list2.extend([0, -1])      # -> [4, 3, 2, 1, 0, -1]
    list1.insert(0, 4.5)       # -> [4.5, 5, 6, 7, 8]
    list1.remove(7)            # remove first 7
    popped = list2.pop(1)      # remove and return index 1
    list1.reverse()            # in-place reverse
    list2.sort()               # in-place sort

    print(list1, list2, popped)

