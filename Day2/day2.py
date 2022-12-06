def split_to_pairs(s):
    return s.split(' ')

if __name__ == '__main__':
    fn = 'day3_input.txt'
    with open(fn) as f:
        lines = f.read()
    lines = lines.split('\n')
    pairs = list(map(split_to_pairs, lines))

    # beat_combo = {
    #     'X': 'C', # rock beats scissors
    #     'Y': 'A', # paper beats rocks
    #     'Z': 'B', # scissors beats papers
    # }
    #
    # equal_combo = {
    #     'X': 'A',
    #     'Y': 'B',
    #     'Z': 'C'
    # }
    #
    # choice_score = {
    #     'X': 1,
    #     'Y': 2,
    #     'Z': 3
    # }
    #
    # res1 = 0
    #
    # for p in pairs:
    #     res1 += choice_score[p[1]]
    #     if equal_combo[p[1]] == p[0]:
    #         res1 += 3
    #     elif beat_combo[p[1]] == p[0]:
    #         res1 += 6
    #
    # print(res1)

    beat_score = {
        'A': 2,
        'B': 3,
        'C': 1
    }

    choice_score2 = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    lose_score = {
        'A': 3,
        'B': 1,
        'C': 2
    }

    res2 = 0

    for p in pairs:
        if p[1] == 'Y':
            res2 += choice_score2[p[0]] + 3
        elif p[1] == 'Z':
            res2 += beat_score[p[0]] + 6
        elif p[1] == 'X':
            res2 += lose_score[p[0]]
        # print(res2)

    print(res2)
