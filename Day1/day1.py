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

    print(max(res))

    top_3 = [res[0], res[1], res[2]]

    for n in res:
        if n > min(top_3):
            top_3.remove(min(top_3))
            top_3.append(n)

    print(sum(top_3))