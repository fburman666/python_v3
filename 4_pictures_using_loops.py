print("a:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("a:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("c:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or x == 4 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("d:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 or y == 3:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("e:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x + y == 7 or x == 5:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("f:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x + y == 7 or x - y == 0:
            s += "#"
        else:
            s += "."
    print(s)
print("")

print("g:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 == 1:
            s += "#"
        else:
            s += "."
    print(s)
print("")


print("h:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (y == 2 or y == 5) and (2 <= x <= 7):
            s += "#"
        elif (x == 2 or x == 7) and (2 <= y <= 5):
            s += "#"
        else:
            s += "."
    print(s)
print("")



print("i:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (y == 1) or (y == 4):
            if x == 2 or x == 5 or x == 8:
                s += "#"
            elif x == 1 or x == 4 or x == 7:
                s += "."
            else:
                s += "0"
        elif (y == 2) or (y == 5):
            if x == 1 or x == 4 or x == 7:
                s += "0"
            elif x == 2 or x ==5 or x == 8:
                s += "."
            else:
                s += "#"
        else:
            if x == 1 or x == 4 or x == 7:
                s += "#"
            elif x == 2 or x == 5 or x == 8:
                s += "0"
            else:
                s += "."


    print(s)
print("")


print("j:")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if y <= 3:
            if 3 <= x <= 5:
                s += "#"
            else:
                s += "."
        elif 4 == y:
             s += "."
        elif y == 5:
            if x % 2 == 0:
                s += "#"
            else:
                s += "."
        else:
            if x % 2 == 0:
                s += "."
            else:
                s += "#"
    print(s)
print("")
