#jweles and stones

jweles = "aAb"
stones = "aaAAbbbb"
count = 0
for i in stones:
    if i in jweles:
        count+=1
print(count)