#rotate string
def shift (s,goal):
    if len(s) != len(goal):
        print("False")
    else:
        combined = s + s
        if goal in combined:
            print("True")
        else:
            print("False")
s = input("Enter the first string: ")
goal = input("Enter the second string: ")
shift(s, goal)
