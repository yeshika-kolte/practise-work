lst=[1,5,4,6,7,8]
n=len(lst)

if n==1:
    print(f"peak element found at{0}=>{1}")
    #check foe elemnt when its len is 2
elif n==2:
    if lst[0] > lst[1]:
      print(f"peak element found at {0}=>{1}")
    elif lst[0] > lst[1]:
      print(f"peak element found at {1}=>{1}") 
      #check for when list len is more than 2 
elif n>2:
    if lst[n-1] > lst[n-2]:
      print(f"peak element founst at{n-1}=>1") 
      #check for first element  
    elif lst [0]>lst[1]:
       print(f"peak element founst at{0}=>1") 
    else :
     # check for mid element       
        for i in range (1,n-1):
            if lst[i] > lst[i-1] and lst [i] >lst [i+1]:
                print(f"peak element founst at{i}=>1") 
                break 
            else:
                print(f"peak element not found")
             
        
           
          
            