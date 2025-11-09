
def mystery(w):
    a = 0
    v = "aeiouAEIOU"
    for z in w:
        if z in v:
            a += 1
    return a 

x = mystery("HEllo")
print(x)


x = mystery("SupercalifrAgilistIcexpEalidocious")
print(x)
