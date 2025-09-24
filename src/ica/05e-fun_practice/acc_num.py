def sum_range(start_val, end_val):
    # acc_nums.py

    def sum_range(start_val, end_val):
        cnt = 0  # initialize accumulator to default value 0
        for x in range(start_val, end_val + 1):
            cnt = cnt + x  # update: add new x value to old value of cnt
        return cnt

    if __name__ == "__main__":
        # 1) Straightforward example: add numbers in a range
        print("sum_range(1, 5) =", sum_range(1, 5))  # expected 15

        # 2) Start and end are the same
        print("sum_range(7, 7) =", sum_range(7, 7))  # expected 7

        # 3) Start value greater than end value (range is empty → 0 with this function)
        print("sum_range(10, 5) =", sum_range(10, 5))  # expected 0

        # 4) Both values negative
        print("sum_range(-3, 2) =", sum_range(-3, 2))  # expected -3


