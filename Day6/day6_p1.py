if __name__ == '__main__':
    fn = 'day6_input' + '.txt'
    with open(fn) as f:
        inp = f.read()

    left = 0
    unique = set()

    for right in range(4, len(inp)):
        signal = inp[left:right]
        temp = set([letter for letter in signal])
        if len(temp) == 4:
            print(right)
            break
        left += 1

