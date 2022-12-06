def split_pair(s):
    return s.split(',')

if __name__ == '__main__':
    fn = 'd4_input' + '.txt'
    with open(fn) as f:
        lines = f.read()
    lines = lines.split('\n')
    puzzle_input = list(map(split_pair, lines))

    res = 0

    for i in puzzle_input:
        pair_1 = list(map(int, i[0].split('-')))
        pair_2 = list(map(int, i[1].split('-')))

        print(pair_1, pair_2)

        if pair_2[0] <= pair_1[1] <= pair_2[1]:
            res += 1
        elif pair_1[0] <= pair_2[1] <= pair_1[1]:
            res += 1

    print(res)