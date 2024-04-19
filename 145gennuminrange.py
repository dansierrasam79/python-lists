import random
loop_val = 0
while loop_val < 6:
    rand_val = random.randint(1,10)
    if rand_val != 2 and rand_val != 6 and rand_val != 10:
        print(rand_val)
    loop_val += 1