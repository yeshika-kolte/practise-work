d={'a': 1, 'b': 2, 'c': 3}
l= list(d.items())
for i in range(len(l)):
    l[i] = (l[i][1], l[i][0])
print(l)