def num_lines_to_write_string(widths: list, string: str) -> list:
    # checking lenth of input string
    if len(string) < 1 or len(string) > 1000:
        return ["F", "A", "L", "S", "E"]

    # set empty variables
    counter = 0
    list_index = 0
    new_string = ""

    # iterating through each character in input string
    while counter != len(string):
        # adding the result of widths[i] * string[i] to new_string
        new_string += (widths[list_index] * string[list_index])
        # increment both counter and list_index
        counter += 1
        list_index += 1
        if list_index > len(widths):
            # reset list_index to zero if out of range for widths
            list_index = 0

    # return upside-down floor division and modulus
    return [-(-len(new_string) // 100), len(new_string) % 100]


print(num_lines_to_write_string([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                 10, 10, 10, 10], "abcdefghijklmnopqrstuvwxyz"))
