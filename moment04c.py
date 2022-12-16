atot = []


while True:
    print("Denna applikation gör ett antal beräkningar på en rätblock.")


    while True:
        try:
            num1 = int(input("Ange rätblockets ena sida: "))
            num2 = int(input("Ange rätblockets andra sida: "))
            num3 = int(input("Ange rätblockets höjd: "))

            break

        except ValueError:
            print("Det är inget nummer!")

    if num1 < 1:
        num1 = 1
    if num2 < 1:
        num2 = 1
    if num3 < 1:
        num3 = 1


    tot = num1*num2

    atot.append(tot)

    print("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}" .format(num1, num2, tot))
    if num1 == num2:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    else:
        print("Eftersom bägge sidorna inte är lika långa är detta en rektangel")
    print("Höjden | Volymen\n-----------------")

    for i in range(1, num3+1):
        print("{:6} | {:3}".format(i, (i*tot)))

    if input('Vill du göra en beräkning till (J/N)?): ') != 'J':
        print("Alla dina areor på kvadraterna var", atot)
        break