def coins(total):
    total = int(total * 100)
    q = total // 25
    total %= 25
    d = total // 10
    total %= 10
    n = total // 5
    p = total % 5
    return q, d, n, p
#     return (q, d, n, p)
#     return [q, d, n, p]

money = float(input("Enter amount: "))
thing = coins(money)
print(type(thing))
qu, di, ni, pe = thing # unpacking
qu = thing[0]
di = thing[1]
print(qu, di, ni, pe)




