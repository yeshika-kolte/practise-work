for i in range(5, 0, -1):
    
    a = "*" if i % 2 != 0 else "#"
    for j in range(i):
        print(a, end="")
    print()
