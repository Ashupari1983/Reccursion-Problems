def steps(m,n):
    if m ==1 or n ==1:
        return 1
    return steps(m-1,n)+ steps(m,n-1)

x = int(input('Enter number of rows: '))
print('Steps: ',steps(x,x))