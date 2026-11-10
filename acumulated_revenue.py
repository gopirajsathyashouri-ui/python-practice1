revenue = eval(input())
cumulative = []
total = 0
for r in revenue:
    total += r
    cumulative.append(total)
print(cumulative)

