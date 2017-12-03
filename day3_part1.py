import sys
import math

try:
    input_num = int(sys.argv[1])
except Exception as ex:
    sys.stderr.write(str(ex))

input_sqrt_cieled = math.ceil(math.sqrt(input_num))
lower = False # is the number in a lower part of the square
# compute the distance from the square which the number is part of to 1
if input_sqrt_cieled > 2:
    if input_sqrt_cieled % 2 == 0:
        square_distance = input_sqrt_cieled // 2
        lower = True
    else:
        square_distance = (input_sqrt_cieled - 1) // 2
elif input_sqrt_cieled == 2:
    lower = True
    square_distance = 1
elif input_sqrt_cieled == 1:
    print(0)
    exit()

# distance from the numbers at the square corners to 1
max_distance = square_distance * 2

# compute the difference between the highest square number and the input number
if lower:
    difference = (((input_sqrt_cieled + 1) ** 2) - input_num) % max_distance
else:
    difference = ((input_sqrt_cieled ** 2) - input_num) % max_distance

# tmp will be subtracted from max_distance
if difference < square_distance:
    # the number is on the right side / bottom part of row/col
    tmp = difference
elif difference > square_distance:
    # the number is on the left side / top part of row/col
    tmp = abs(square_distance - difference)
    tmp = square_distance - tmp
else:
    # the number is at the center of the row/col of the square
    tmp = square_distance

print(max_distance - tmp)
