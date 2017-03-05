t = int(raw_input())
tl = []
j = 0

while j < t:
    tl.append(raw_input())
    j += 1

for s in tl:
    
    s = list(s)
    lc = 0
    i = 0
    
    for i in range(1,len(s)):
        if s[i] != s[i - 1]:
            None
        else:
            lc += 1
    print lc