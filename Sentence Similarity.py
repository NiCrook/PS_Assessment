def sentence_similary(words1: list, words2: list, pairs: list) -> bool:
    # checking all test cases
    if len(words1) > 1000 or len(words2) > 1000:
        return False
    if len(pairs) > 2000:
        return False
    for pair in pairs:
        if len(pair) < 2 or len(pair) > 2:
            return False
        for word in pair:
            if len(word) < 1 or len(word) > 20:
                return False
    for word in words1:
        if len(word) < 1 or len(word) > 20:
            return False
    for word in words2:
        if len(word) < 1 or len(word) > 20:
            return False

    # checking lengths and equivalences
    if len(words1) != len(words2):
        return False
    if words1 == words2:
        return True

    # create placeholder variable
    counter = 0
    # using counter, iterate through length of either word list
    while counter != len(words1):
        # if iterated words are not similar, return False
        if words1[counter] != pairs[counter][0] or words2[counter] != pairs[counter][1]:
            return False
        counter += 1

    # if we hit this point, it's because we haven't run into anything that's given a false
    # so with no logic left to run, we return True
    return True


print(sentence_similary(
    ["great", "acting", "skills"],
    ["fine", "drama", "talent"],
    [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]))
