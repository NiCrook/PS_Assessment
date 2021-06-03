def rotate_digits(num: int) -> int:
    # create check for num value
    if num < 0 or num > 10000:
        return 0

    # create list of bad numbers because these are known
    bad_numbers = [0, 1, 3, 4, 7, 8]
    # create placeholder variables
    counter = 0
    good_numbers = 0

    # iterate through range of num
    while counter != num:
        # convert int to list of string characters
        new_list = [i for i in str(counter)]
        # iterate through each element in new_list
        for i in new_list:
            # check if converted string to integer element is in bad_numbers list
            if int(i) in bad_numbers:
                # if so, simply increment counter by one
                counter += 1
            else:
                # if not, then increment both good_numbers and counter by one
                good_numbers += 1
                counter += 1

    return good_numbers


print(rotate_digits(10))
