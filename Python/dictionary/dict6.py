#swapping tuples in dictionary
data = {'a':1, 'b':2, 'c':3}
l= list(data.items())
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][1] > l[j][1]:
            l[i], l[j] = l[j], l[i]
print(f"Swapped tuples: {l}")           