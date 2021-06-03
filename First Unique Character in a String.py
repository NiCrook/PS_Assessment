def first_unique(word: str) -> int:
    # create placeholder variables
    cur_ind = 0
    counter = 1

    # iterate through length of word
    try:
        while cur_ind != len(word):
            if word[cur_ind] == word[counter]:
                cur_ind += 1
                counter = cur_ind + 1
            elif word[cur_ind] != word[counter]:
                counter += 1
                if counter > len(word) - 1:
                    return cur_ind
    except IndexError as err:
        print("No uniques found")


print(first_unique("leetcode"))
print(first_unique("loveleetcode"))
