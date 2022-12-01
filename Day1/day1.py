def split_line(s):
    nums = s.split('\n')
    return list(map(to_int, nums))


def to_int(s):
    return int(s);


if __name__ == '__main__':
    with open('day1_input.txt') as f:
        lines = f.read()
    lines = lines.split('\n\n')

    arr = list(map(split_line, lines))
    res = list(map(sum, arr))
    print(res, '\n', max(res))
