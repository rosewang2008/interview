def array_left_rotation(a, n, k):
    if n == k:
        return ''.join(str(x) for x in a)
    elif k == 0:
        return ''.join(str(x) for x in a)
    else:
        new_array = a[k:]
        added = a[:k]
        new_array = new_array + added
        return ''.join(str(x) for x in new_array)
    
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')