from random import random
maxnum = 10000
def in_circle (x,y):
    return x∗∗2 + y∗∗2 <= 1
def calculate_pi (maxnum ):
    hit_count = 0
    for _ in range(1, maxnum ):
    if in_circle (random (), random ()):
    hit_count += 1
    return 4.∗ hit_count /maxnum

in_circle()
calculate_pi (maxnum )