s1= "listen"
s2= "selent"
if len(s1) != len(s2):
    print("Not anagrams")
else:
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq:
            print("Not anagrams")
            break
        freq[ch] -= 1
        if freq[ch] < 0:
            print("Not anagrams")
            break
    else:
        print("Anagrams")