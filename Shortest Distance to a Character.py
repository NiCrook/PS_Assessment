def shortest_distance(word: str, letter: str) -> list:
    shortest_list = []
    cur_ind = 0
    counter = 0

    while cur_ind != len(word):
        # check if current index is equal to letter
        if word[cur_ind] == letter:
            # current index is equal to letter
            # append, increment, reset
            shortest_list.append(counter)
            cur_ind += 1
            counter = 0
        else:
            # current index is not equal to letter
            counter += 1
            # begin checking edges
            # check if left edge out of range
            if cur_ind + (counter * -1) < 0:
                while word[cur_ind + counter] != letter:
                    counter += 1
                # edge character is equal to letter
                # append, increment, reset
                shortest_list.append(counter)
                cur_ind += 1
                counter = 0
            # chec if right edge out of range
            elif cur_ind + counter > len(word) - 1:
                # check while left edge character is not letter
                while word[cur_ind + (counter * -1)] != letter:
                    counter += 1
                # edge character is equal to letter
                # append, increment, reset
                shortest_list.append(counter)
                cur_ind += 1
                counter = 0
            else:
                # edges in range
                # checking for both edges to be not equal to letter
                while word[cur_ind + counter] != letter and word[cur_ind + (counter * -1)] != letter:
                    counter += 1
                    # check if left edge out of range
                    if cur_ind + (counter * -1) < 0:
                        while word[cur_ind + counter] != letter:
                            counter += 1
                        shortest_list.append(counter)
                        cur_ind += 1
                        counter = 0
                    # check if right edge out of range
                    elif cur_ind + counter > len(word) - 1:
                        while word[cur_ind + (counter * -1)] != letter:
                            counter += 1
                        # edge character is equal to letter
                        # append, increment, reset
                        shortest_list.append(counter)
                        cur_ind += 1
                        counter = 0
                # edge character is equal to letter
                # apppend, increment, reset
                shortest_list.append(counter)
                cur_ind += 1
                counter = 0
    # loop complete
    else:
        return shortest_list


print(shortest_distance("loveleetcode", "e"))
