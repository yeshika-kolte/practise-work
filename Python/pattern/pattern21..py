seq = "1"
for i in range(10):
    print(seq)
    seq += "0" if i % 2 == 0 else "1"
