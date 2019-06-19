colors = ['black','white']
sizes = ['s','m','l']
# 1
t = [(c,s) for c in colors for s in sizes]
print(t)
# 2
for c in colors:
    for s in sizes:
        print(c,s)
# 3
