import sys

input_nums = []

for num in sys.argv[1]:
    input_nums.append(int(num))

def first_part():
    prev_num = 0
    sum_ = 0
    for num in input_nums:
        if num == prev_num:
            sum_ += num
        prev_num = num
    if num == input_nums[0]:
        sum_ += num
    return sum_

def second_part():
    sum_ = 0
    len_ = len(input_nums)
    half = int(len_ / 2)
    index = 0
    step = 0
    for num in input_nums:
        index = (step + half) % len_
        if num == input_nums[index]:
            sum_ += num
        step += 1
    return sum_

#print(first_part())
print(second_part())
