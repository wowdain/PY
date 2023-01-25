def calculate_fee(*ages): #ages는 튜플
    total = 0
    for age in ages :
        if 19 <= age : #adult
            total += 10000
        else :
            total += 4000
    return total

print(calculate_fee(21, 25, 20))
print(calculate_fee(7, 45, 43, 10))