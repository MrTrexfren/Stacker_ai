import random
import time
import numpy as np

blocks = [1, 2, 3]
block_pos = ["left", "middle", "right"]

tower = [0]
tower_mass = 0

placed = True
tower_fell = False


stack_until = input("Stack Until: ")

for n in range(int(stack_until)):
    falling_point = np.median(tower_mass)
    new_block = random.choice(blocks)
    prev_block = n - 1
    new_pos = random.choice(block_pos)

    tower.append(new_block)

    if tower_fell != True:
        # Tower placement probability
        if tower[n] == 1 or tower[n] == 2 or tower[n] == 3 and tower[
            prev_block] == 1 and new_pos == "left" or new_pos == "right":
            placed = False
        elif tower[n] == 1 or tower[n] == 2 or tower[n] == 3 and tower[prev_block] == 2 and new_pos == "middle":
            placed = True

        if tower[n] == 1 or tower[n] == 2 or tower[n] == 3 and tower[
            prev_block] == 2 and new_pos == "left" or new_pos == "right":
            placed = False
        elif tower[n] == 1 or tower[n] == 2 and tower[prev_block] == 2 and new_pos == "middle":
            placed = True

        if tower[n] == 1 or tower[n] == 2 and tower[prev_block] == 3 and new_pos == "left" or new_pos == "right":
            placed = True
        elif tower[n] == 3 and tower[prev_block] == 3 and new_pos == "middle":
            placed = True

        print("New Block Size:", tower[n], " New Block Position:", new_pos, " Placed:", placed)
        n += 1

    time.sleep(1)

print("Tower Succeded!")
