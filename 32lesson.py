import random

a = [random.randint(1, 10) for i_counter in range(5)]

print(a)

for j_index in range(1, 5):
    for i_index in range(5 - j_index):
        if a[i_index] > a[i_index + 1]:
            a[i_index], a[i_index+1]=a[i_index+1], a[i_index]
print(a)
