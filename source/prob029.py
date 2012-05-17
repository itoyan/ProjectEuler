
ans = []

for a in range(2, 101):
    for b in range(2, 101):
        num = a ** b
        if not num in ans:
            ans.append(num)

print len(ans)
