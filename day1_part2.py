import sys

sum_ = 0
len_ = len(sys.argv[1])
half = len_ // 2
step = 0
for num in sys.argv[1]:
    if num == sys.argv[1][(step + half) % len_]:
        sum_ += int(num)
    step += 1
print(sum_)
