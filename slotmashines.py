# The game represents a real-life slot machine, the player can decide the amount to start betting with and how many lines to bet on.
# The player can continue to bet until he/she runs out of money

import random


def validateF(x):
    if x == "p":
        return True


def validateS(x):
    if x.isdigit():
        return True
    else:
        print("Invalid input, must be a number.")
        return False


def validateT(x):
    if x.isdigit() and int(x) in range(1, 4):
        return True
    else:
        print("Invalid input, must be a number between 1 and 3. ")
        return False


def dollarslinetotal(x, y):
    z = int(x) * int(y)
    print(f"You are betting {x} on {y} of lines. The total bet is equal to {z} dollars.")


def moneyearned(count):
    global userLines
    global userBetOnEachLine
    userLines = int(userLines)
    userBetOnEachLine = int(userBetOnEachLine)
    if count == 0:
        sumMoney = -1 * userLines * userBetOnEachLine
    elif count < userLines:

        takeout = (count - userLines) * userBetOnEachLine
        if count > 0:
            add = count * userBetOnEachLine
        else:
            add = 0
        sumMoney = takeout + add
    elif count > userLines:
        takeout = (userLines - count) * userBetOnEachLine
        if count > 0:
            add = userLines * userBetOnEachLine
        else:
            add = 0
        sumMoney = add + takeout

    elif count == userLines:
        sumMoney = userLines * userBetOnEachLine

    return sumMoney


def slotcount():
    count = 0
    listA = ["A", "B", "C", "D"]
    _11 = listA[random.randint(0, 3)]
    _12 = listA[random.randint(0, 3)]
    _13 = listA[random.randint(0, 3)]
    # ---
    _21 = listA[random.randint(0, 3)]
    _22 = listA[random.randint(0, 3)]
    _23 = listA[random.randint(0, 3)]
    # ---
    _31 = listA[random.randint(0, 3)]
    _32 = listA[random.randint(0, 3)]
    _33 = listA[random.randint(0, 3)]
    # ---
    _41 = listA[random.randint(0, 3)]
    _42 = listA[random.randint(0, 3)]
    _43 = listA[random.randint(0, 3)]
    # ---
    _51 = listA[random.randint(0, 3)]
    _52 = listA[random.randint(0, 3)]
    _53 = listA[random.randint(0, 3)]
    # ---
    _61 = listA[random.randint(0, 3)]
    _62 = listA[random.randint(0, 3)]
    _63 = listA[random.randint(0, 3)]
    print(f"{_11}|{_12}|{_13}")
    print(f"{_21}|{_22}|{_23}")
    print(f"{_31}|{_32}|{_33}")
    print(f"{_41}|{_42}|{_43}")
    print(f"{_51}|{_52}|{_53}")
    print(f"{_61}|{_62}|{_63}")
    if _11 == _12 == _13:
        count += 1
    if _21 == _22 == _23:
        count += 1
    if _31 == _32 == _33:
        count += 1
    if _41 == _42 == _43:
        count += 1
    if _51 == _52 == _53:
        count += 1
    if _61 == _62 == _63:
        count += 1
    return count


playOrQuit = input("Press enter to play or q to quit: ")
userDeposit = input("Enter the amount you want to deposit: $")
currentBalance = int(userDeposit)
while playOrQuit != " ":
    if validateF(playOrQuit):
        userLines = input("Enter the number of lines you want to bet on (1-3): ")
        userBetOnEachLine = input("How much would you like to bet on each line: $")
        if validateS(userDeposit) and validateT(userLines) and validateS(userBetOnEachLine):
            dollarslinetotal(userBetOnEachLine, userLines)
            count = slotcount()
            if moneyearned(count) > 0:
                print(f"You won {moneyearned(count)} dollars")
            elif moneyearned(count) < 0:
                print(f"You lost {moneyearned(count)} dollars")
            currentBalance = moneyearned(count) + currentBalance
            print(f"Your current balance is {currentBalance}")
            if currentBalance <= 0:
                print("You ran out of money, better luck next time!")
                break
    else:
        print(f"The game will stop now, your balance is {currentBalance}")
        break
    playOrQuit = input("Press enter to play or q to quit: ")
