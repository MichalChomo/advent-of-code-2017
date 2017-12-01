import sys

sum_ = 0
len_ = len(sys.argv[1])
half = int(len_ / 2)
index = 0
step = 0
for num in sys.argv[1]:
    intnum = int(num)
    index = (step + half) % len_
    if intnum == int(sys.argv[1][index]):
        sum_ += intnum
    step += 1
print(sum_)
