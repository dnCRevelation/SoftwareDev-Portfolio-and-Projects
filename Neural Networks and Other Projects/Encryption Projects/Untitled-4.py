def is_staircase(nums):
    col_length = 0
    staircase = []

    while len(nums) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(nums.pop(0))

            if (len(nums) == 0):
                if i < col_length - 1:
                    return False
                return staircase
        staircase.append(column)