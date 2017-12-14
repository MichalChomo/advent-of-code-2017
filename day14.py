import day10

def in_bounds(x):
    return x >= 0 and x < 128

def dfs(y, x):
    global bin_hashes
    if (not in_bounds(y)) or (not in_bounds(x)) or bin_hashes[y][x] == 0:
        return
    bin_hashes[y][x] = 0
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)


key = "jzgqcdpd"
bin_hashes = []
for i in range(128):
    bin_hash = ""
    for x in day10.knot_hash(key + '-' + str(i)):
        bin_hash += "{0:04b}".format(int(x, 16))
    bin_hashes.append([int(x) for x in bin_hash])
print(sum([h.count(1) for h in bin_hashes]))

regions = 0
for y in range(128):
    for x in range(128):
        if bin_hashes[y][x] == 1:
            regions += 1
            dfs(y, x)
print(regions)
