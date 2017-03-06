# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for val in range(n):
    if val == 0:
        g = set(raw_input())
    else:
        g = g.intersection(set(raw_input()))
print len(g)