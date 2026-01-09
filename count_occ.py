def count_occ(sentence="brice", char='c'):
    count = 0
    for i in range(1, len(sentence)):
        if sentence[i] == char:
            count += 1
    return count
