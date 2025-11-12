gas = {"Casey's" : 2.46,
       "Costco" : 2.46,
       "Amoco" : 3.69,
       "Bob's Place" : 1.23,
       "Other Place" : 2.47,
       }


#print("12345678901234567890")
print(f"{'Location':12}{'Price':>6}")
for loc in gas:
    print(f"{loc:12}{gas[loc]:6.2f}")
    
    
    
    #print(f"{loc:12}{gas[loc]:2.6f}")
    #print(f"{loc:>12}{gas[loc]:^6.2f}")
    #print(f"{loc:^12}{gas[loc]:6.2f}")
