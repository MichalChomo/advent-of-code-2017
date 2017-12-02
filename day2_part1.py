def get_intlist(line):
    strlist = line.split('\t')
    return [int(x) for x in strlist]


def get_max_min_diff(line):
    intlist = get_intlist(line)
    return (max(intlist)) - (min(intlist))


if __name__ == '__main__':
    with open("day2_part1_input", 'r') as infile:
        total = 0
        for line in infile:
            line = line.replace('\n', '')
            if len(line) != 0:
                total += get_max_min_diff(line)

        print(total)
