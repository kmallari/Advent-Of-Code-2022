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
    res = []

    for rucksack in lines:
        length = len(rucksack)
        s1 = set()
        s2 = set()
        for i in range(int(length / 2)):
            s1.add(rucksack[i])
        for j in range(int(length / 2), length):
            s2.add(rucksack[j])

        priority = priority_convert(s1.intersection(s2).pop())
        res.append(priority)

    print(sum(res))
