if __name__ == '__main__':
    fn = 'day5_input' + '.txt'
    with open(fn) as f:
        lines = f.read()
    lines = lines.split('\n')
    temp_stack = []
    for l in lines:
        if l == '':
            break
        temp_stack.append(l + ' ')

    # for i in range(0, len(temp_stack) - 3, 3):
    num_of_col = int(temp_stack[-1][-2])

    temp_stack2 = []

    for row in temp_stack[0:-1]:
        temp = []
        for i in range(0, len(row) - 3, 4):
            temp.append(row[i:i + 4][1])
        temp_stack2.append(temp)

    # temp_stack3 =

    stack = []

    for i in range(len(temp_stack2[-1])):
        col = []
        for j in range(len(temp_stack2) - 1, -1, -1):
            try:
                col.append(temp_stack2[j][i])
            except:
                col.append(' ')
        stack.append(col)

    moves = []

    for line in lines:
        temp = []
        if line.startswith('move'):
            temp.append(int(line.split(' ')[1]))
            temp.append(int(line.split(' ')[3]))
            temp.append(int(line.split(' ')[5]))
            moves.append(temp)

    final_stack = []

    for i in stack:
        temp = []
        for j in i:
            if j != ' ':
                temp.append(j)
        final_stack.append(temp)

    for move in moves:
        __to__ = move[2] - 1
        __from__ = move[1] - 1
        __count__ = move[0]
        i = 0

        while i < __count__:
            final_stack[__to__].append(final_stack[__from__].pop())
            i += 1

    res = ''

    for i in final_stack:
        res += i[-1]

    print(res)



