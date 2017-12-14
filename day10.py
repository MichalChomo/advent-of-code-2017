def knot_hash_round(hash_input, circle, cur_pos, skip_size):
    for h in hash_input:
        if (cur_pos + h) > len(circle):
            sublist = circle[cur_pos:] + circle[:(cur_pos + h) % len(circle)]
            sublist.reverse()
            circle[cur_pos:] = sublist[:len(circle)-cur_pos]
            if h > len(circle):
                circle_sublist_end = h - len(circle)
            else:
                circle_sublist_end = h - (len(circle) - cur_pos)
            circle[:circle_sublist_end] = sublist[len(circle)-cur_pos:]
        else:
            if h > 1:
                sublist = circle[cur_pos:(cur_pos+h)]
                sublist.reverse()
                circle[cur_pos:(cur_pos+h)] = sublist
        cur_pos = (cur_pos + h + skip_size) % len(circle)
        skip_size += 1
    return (circle, cur_pos, skip_size)

def knot_hash(hash_input):
    skip_size = 0
    cur_pos = 0
    circle = [i for i in range(256)]
    hash_input_list = [ord(x) for x in hash_input] + [17, 31, 73, 47, 23]
    for _ in range(64):
        (circle, cur_pos, skip_size) = knot_hash_round(hash_input_list, circle, cur_pos, skip_size)
    chunks = [circle[i*16 : i*16+16] for i in range(16)]
    dense_hash = []
    for chunk in chunks:
        xored = 0
        for num in chunk:
            xored ^= num
        dense_hash.append(xored)
    return "".join("%02x"%num for num in dense_hash)

if __name__ == "__main__":
    with open("day10_input") as infile:
        lengths = list(map(int, infile.readline().split(',')))
    skip_size = 0
    cur_pos = 0
    circle = [i for i in range(256)]
    (circle, _, _) = knot_hash_round(lengths, circle, 0, 0)
    print(circle[0] * circle[1])

    with open("day10_input") as infile:
        lengths2 = infile.readline().strip()
    print(knot_hash(lengths2))
