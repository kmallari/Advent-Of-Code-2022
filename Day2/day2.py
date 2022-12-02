def split_to_pairs(s):
    return s.split(' ')

if __name__ == '__main__':
    fn = 'day2_input.txt'
    with open(fn) as f:
        lines = f.read()
    lines = lines.split('\n')
    pairs = list(map(split_to_pairs, lines))

    beat_combo = {
        'X': 'C', # rock beats scissors
        'Y': 'A', # paper beats rocks
        'Z': 'B', # scissors beats papers
    }

    equal_combo = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    choice_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    res = 0

    for p in pairs:
        res += choice_score[p[1]]
        if equal_combo[p[1]] == p[0]:
            res += 3
        elif beat_combo[p[1]] == p[0]:
            res += 6

    print(res)
