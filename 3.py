a = int(input())
b = {}

for i in range(a):
    r = input()
    
    if 'drove into place' in r:
        b[r.split()[0]] = r.split()[-1]
    elif 'drove out' in r:
        del b[r.split()[0]]
    else:
        r = r.split()
        if r[-1] in b:
            print(b[r[-1]])
        else:
            print('Not here')
