mod = 2147483647
total = 0
val_a = 722
val_b = 354
for _ in range(40000000):
    val_a = (val_a * 16807) % mod
    val_b = (val_b * 48271) % mod
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print(total)
total = 0
val_a = 722
val_b = 354
for _ in range(5000000):
    val_a = (val_a * 16807) % mod
    while (val_a % 4) != 0:
        val_a = (val_a * 16807) % mod
    val_b = (val_b * 48271) % mod
    while (val_b % 8) != 0:
        val_b = (val_b * 48271) % mod
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print(total)
