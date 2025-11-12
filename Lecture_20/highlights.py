# highlights from lecture 20


# print("Hello")   # default parameters
# print("Hi there",4,6,1234.2,[5,6,7,8], end=" --- ") # keyword arguments
# print("how are you?")
# 
# input()

# # immutable
# x = 10
# print(x, id(x))
# x = 12
# print(x, id(x))
# 
# 
# # mutable
# y = [10, 20, 30]
# print(y, id(y))
# y[2] = 40
# print(y, id(y))
# 
# input()

# # a is immutable, assuming it's an int, float, string, Boolean
# def foo(a):
#     a *= 2
#     
# g = 10
# print(g)
# foo(g)
# print(g)
# 
# input()

# # b is mutable, assuming it's a list or dictionary
# def bar(b):
#     b[2] = 651
#     
# f = [ 1, 2, 3 ]
# print(f)
# bar(f)
# print(f)
# 
# input()

def bar(b):
    b[2] = 651
    
dont_change_me = [ 1.23, 5.78, 1882 ]
print(dont_change_me)
bar(dont_change_me[:])    # prevent mutability of the list with [:]
print(dont_change_me)
bar(dont_change_me[:])
print(dont_change_me)



