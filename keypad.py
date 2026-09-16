
keys = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 

def key(a):
    if len(a) == 0:
        return 1
    return len(keys[a[0]]) * key(a[1:])

x = input('Enter keys combo: ')
print('No. of possible alphabet combos: ',key(x))