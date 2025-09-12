devisor = int(input())
boundary = int(input())

largest_devisee = 0

for i in range(1, boundary + 1):
    if i % devisor == 0:
        largest_devisee = i

if largest_devisee > 0:
    print(largest_devisee)