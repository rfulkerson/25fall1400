foo = 21.12 # global variable

def function_a():  # global function
    x = 12    # local variable
    print("global", foo)
    print("function_a x", x)

def function_b():  # global function
    y = 42.123  # local variable
    print("function_b y", y)
    for z in range(6):    # z is local to function, range is a built-in function
        print("function_b z in loop", z)
    print("function_b z after loop", z)
    function_a()

if __name__ == '__main__':
    z = int(input())  # local variable
    print("main z", z)  # print is a built-in scope function
    function_a()
    function_b()
    print("main z", z)  # print is a built-in scope function
    
