import random

start_list = [random.randint(1, 100) for randomize in range(100)]

sort_list = sorted(start_list)

print(f'Значения в порядке возрастания {sort_list}\n\n\n')
print(f'Значения в порядке убывания {sort_list[::-1]}')
