def array_left_rotation(a, n, k):
    if k > n:
        k = k % n
    a1 = a[0:k]
    a2 = a[k::]
    return a2 + a1  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))