def hanoi(x):
    if x == 0:
        return 0
    return 2*hanoi(x-1) +1

a = int(input('Enter number of disks: '))
print('Steps: ',hanoi(a))