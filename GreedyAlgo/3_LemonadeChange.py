def lemonadeChange(bill):
    # pay[0] = 5, pay[1] = 10, pay[2] = 20
    pay = [0] * 3

    for i in range(len(bill)):
        if bill[i] == 5:
            pay[0] += 1

        elif bill[i] == 10:
            if pay[0] != 0:
                pay[0] -= 1
                pay[1] += 1
            else:
                return False

        else:
            if pay[0] != 0 and pay[1] != 0:
                pay[0] -= 1
                pay[1] -= 1
                pay[2] += 1
            elif pay[0] >= 3:
                pay[0] -= 3
                pay[2] += 1
            else:
                return False
    return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    print(lemonadeChange(bills))

