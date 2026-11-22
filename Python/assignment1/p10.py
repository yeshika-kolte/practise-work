value = input('enter any value:');
if(value == 'null'):
    print("condition-1 value is falsy");
elif((value == "false")):
    print("conditin-2 value is falsy")
elif(not (int(value))):
    print(" condition-3 value is falsy");
elif(value):
    print("condition-4 value is truthy")
else:
    print('condition-5 value is falsy')