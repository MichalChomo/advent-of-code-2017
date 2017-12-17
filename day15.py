(mod, fac_a, fac_b) = (2147483647, 16807, 48271)
(total, val_a, val_b) = (0, 722, 354)
for _ in range(40000000):
    val_a = (val_a * fac_a) % mod
    val_b = (val_b * fac_b) % mod
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print(total)
(total, val_a, val_b) = (0, 722, 354)
for _ in range(5000000):
    val_a = (val_a * fac_a) % mod
    while (val_a % 4) != 0:
        val_a = (val_a * 16807) % mod
    val_b = (val_b * fac_b) % mod
    while (val_b % 8) != 0:
        val_b = (val_b * fac_b) % mod
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print(total)
