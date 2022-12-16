_tot = []
while True:
    print("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
    num1 = int(input("Ange rektangelns ena sida: "))
    num2 = int(input("Ange rektangelns andra sida: "))

    tot = num1*num2
    _tot.append(tot)
    print("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}" .format(num1, num2, tot))
    if num1 == num2:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    else:
        print("Eftersom bägge sidorna inte är lika långa är detta en rektangel")
    print("Höjden | Volymen\n-----------------")

    for i in range(1, 10):
        print("{:6} | {:3}".format(i, (i*tot)))

    if input('Vill du göra en beräkning till (J/N)?): ') != 'J':
        print("Alla dina areor på kvadraterna var", _tot)
        break