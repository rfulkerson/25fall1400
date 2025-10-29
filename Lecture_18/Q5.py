def calculate(a, b):
    return (a + b) * 2

def gen_result(a, b):
    return calculate(a, b) * 2

if __name__ == '__main__':
    print(gen_result(4, 4))
