step = 376
buf = [0]
pos = 0

for i in range(1, 2018):
    pos = ((pos + step) % i) + 1
    buf.insert(pos, i)
print(buf[buf.index(2017) + 1])
pos = 0
for i in range(1, 50000000):
    pos = ((pos + step) % i) + 1
    if pos == 1:
        res = i
print(res)
