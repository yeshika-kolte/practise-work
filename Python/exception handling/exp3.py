def f1():
    try:
        print("Inside try")
        # print (100/0)
        return 100

    except Exception as e:
        print("Exception")
        return 200

    finally:
        return 300
    return 400    

print(f1())