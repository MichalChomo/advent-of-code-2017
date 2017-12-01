import sys

prev_num = '0'
sum_ = 0
for num in sys.argv[1]:
    if num == prev_num:
        sum_ += int(num)
    prev_num = num
if prev_num == sys.argv[1][0]:
    sum_ += int(prev_num)
print(sum_)

