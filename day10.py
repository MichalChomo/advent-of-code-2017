def knot_hash_round(lengths, circle):
    global CIRCLE_LEN
    global cur_pos
    global skip_size
    for length in lengths:
        if (cur_pos + length) > CIRCLE_LEN:
            sublist = circle[cur_pos:] + circle[:(cur_pos + length) % CIRCLE_LEN]
            sublist.reverse()
            circle[cur_pos:] = sublist[:CIRCLE_LEN-cur_pos]
            if length > CIRCLE_LEN:
                circle_sublist_end = length - CIRCLE_LEN
            else:
                circle_sublist_end = length - (CIRCLE_LEN - cur_pos)
            circle[:circle_sublist_end] = sublist[CIRCLE_LEN-cur_pos:]
        else:
            if length > 1:
                sublist = circle[cur_pos:(cur_pos+length)]
                sublist.reverse()
                circle[cur_pos:(cur_pos+length)] = sublist
        cur_pos = (cur_pos + length + skip_size) % CIRCLE_LEN
        skip_size += 1
    return circle


with open("day10_input") as infile:
    lengths = list(map(int, infile.readline().split(',')))
CIRCLE_LEN = 256
skip_size = 0
cur_pos = 0
circle = [i for i in range(CIRCLE_LEN)]
circle = knot_hash_round(lengths, circle)
print(circle[0] * circle[1])

with open("day10_input") as infile:
    lengths2 = [ord(x) for line in infile for x in line]
lengths2 += [17, 31, 73, 47, 23]
skip_size = 0
cur_pos = 0
circle = [i for i in range(CIRCLE_LEN)]
for _ in range(64):
    circle = knot_hash_round(lengths2, circle)
chunks = [circle[i*16 : i*16+16] for i in range(16)]
dense_hash = []
for chunk in chunks:
    xored = 0
    for num in chunk:
        xored ^= num
    dense_hash.append(xored)
print("".join("%02x"%num for num in dense_hash))
