def count_segments(words: str) -> int:
    words = words.split()
    return len(words)


print(count_segments("Hello, my name is John"))
