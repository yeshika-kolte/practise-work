# A    
# AB   
# A C  
# A  D 
# ABCDE

for i in range(65, 70):
    for j in range(65, 70):
        if j == 65 or i == j or i == 69:
            print(chr(j), end="")
        else:
            print(" ", end="")
    print()
