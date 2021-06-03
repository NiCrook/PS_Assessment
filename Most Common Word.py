import string


def most_common_word(paragraph: str, banned: list) -> str:
    # checking len of paragraph
    if len(paragraph) < 0 or len(paragraph) > 1000:
        return "False"
    # checking len of banned
    if len(banned) < 0 or len(banned) > 100:
        return "False"
    # checking len of words in banned
    for banned_word in banned:
        if len(banned_word) < 0 or len(banned_word) > 10:
            banned.remove(banned_word)
    # parse paragraph into list
    parsed_words = list(paragraph.split())
    word_count = {}
    for word in parsed_words:
        # strip word of punctuation and lowercase it
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.lower()
        if word not in banned:
            # increment related dict value by one
            word_count[word] = word_count.get(word, 0) + 1
    # sort dict by values
    word_count = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1])}
    ### I am having trouble ensuring the uniqueness of the max value
    return max(word_count, key=word_count.get)


print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.",
                       ["hit"]))
