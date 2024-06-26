def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    mode_num = 1
    mode_num_value = 1
    for num in nums:
        if nums.count(num) > mode_num_value:
            mode_num = num
            mode_num_value = nums.count(num)
    return mode_num