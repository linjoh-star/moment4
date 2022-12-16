atot = []
num1tot = []


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
    num1tot.append([num1, num2, num3])
    print("Rektangeln har sidorna {0} och {1} vilket gör att arean är {2}".format(num1, num2, tot))
    if num1 == num2:
        print("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    else:
        print("Eftersom bägge sidorna inte är lika långa är detta en rektangel")
    if input('Vill du göra en beräkning till (J/N)?): ') != 'J':
        break

print("Sidlängder| Volymen\n-----------------")
for i in num1tot:
    print(i, i[0]* i[1] * i[2])

print("Alla dina areor på kvadraterna var", atot)
print("Medelvärdet av dina areor är", sum(atot)/len(atot))