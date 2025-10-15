# pythagorean triples!

size = 500
howmany = 0

print(f"testing {size**3} possibilities:")
for a in range(1,size+1):
    for b in range(1,size+1):
        for c in range(1,size+1):
            #print(a,b,c)
            if a**2 + b**2 == c**2:
                #print(a,b,c)
                howmany += 1
                
print(f"found {howmany} triples!")