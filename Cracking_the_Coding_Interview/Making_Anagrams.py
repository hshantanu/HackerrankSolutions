def number_needed(a, b):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    cnt = 0
    for val in chars:
        cnt += abs(a.count(val) - b.count(val))
    return cnt
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)