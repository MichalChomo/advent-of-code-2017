import sys

prev_num = 0
sum_ = 0
for num in sys.argv[1]:
    intnum = int(num)
    if intnum == prev_num:
        sum_ += intnum
    prev_num = intnum
if prev_num == int(sys.argv[1][0]):
    sum_ += prev_num 
print(sum_)

