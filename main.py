str = "+---+---+---------+"
str2 = "| A | B | f(A, B) |"

def func_kon(a, b):
    if (a and b):
        return 1
    else:
        return 0
def func_diz(a, b):
    if (a or b):
        return 1
    else:
        return 0
def func_imp(a, b):
    if (a <= b):
        return 1
    else:
        return 0
def func_ekvi(a, b):
    if (a == b):
        return 1
    else:
        return 0
def func_invkon(a, b):
    if (not a and not b):
        return 1
    else:
        return 0
def func_invdiz(a, b):
    if (not a or not b):
        return 1
    else:
        return 0
print("Таблица истинности для конъюнкции: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_kon(a, b), "   |")
print("Таблица истинности для дизъюнкции: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_diz(a, b), "   |")
print("Таблица истинности для импликации: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_imp(a, b), "   |")
print("Таблица истинности для эквивалентности: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_ekvi(a, b), "   |")
print("Таблица истинности для дизъюнкции инверсмивных переменнных: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_invdiz(a, b), "   |")
print("Таблица истинности для конъюнкции инверсивных пременнных: ")
for x in range(0, 5):
    if (x == 0 or x == 2 or x == 4):
        print(str)
    elif (x == 1):
        print(str2)
    else:
        for a in range(0, 2):
            for b in range(0, 2):
                print("|", a, "|", b, "|   ", func_invkon(a, b), "   |")







