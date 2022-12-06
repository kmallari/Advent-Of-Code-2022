def priority_convert(letter):
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


if __name__ == '__main__':
    fn = 'day3_input.txt'
    with open(fn) as f:
        lines = f.read()
    lines = lines.split('\n')
    f_input = []
    i = 0
    temp = []
    for rucksack in lines:
        temp.append(rucksack)
        i += 1
        if i == 3:
            f_input.append(temp)
            temp = []
            i = 0

    print(f_input)

    res = []

    for group in f_input:
        e = [set(), set(), set()]
        for i, elf in enumerate(group):
            for item in elf:
                e[i].add(item)

        priority = priority_convert(e[0].intersection(e[1]).intersection(e[2]).pop())
        res.append(priority)

    print(sum(res))
