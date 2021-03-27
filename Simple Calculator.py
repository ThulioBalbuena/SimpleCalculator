choose = int(input('OK, lets choose a math operation? addition = 1, subtraction = 2, mutiplication = 3, division = 4, to get out from the operation menu you can type 5 '))
num1 = float(input("Please insert a number"))
num2 = float(input("Please insert another number"))

if choose == 1:
    answer = num1 + num2
    print(answer)
if choose == 2:
    answer = num1 - num2
    print(answer)
if choose == 3:
    answer = num1 * num2
    print(answer)
if choose == 4:
    answer = num1 / num2
    print(answer)

again = input('Do you want to do another operation?')
while again == 'yes':
    choose = int(input('OK, lets choose a math operation? addition = 1, subtraction = 2, mutiplication = 3, division = 4, to get out from the operation menu you can type 5 '))
    if choose == 5:
        print('The program is finished')
        break
    else:
        num1 = float(input("Please insert a number"))
        num2 = float(input("Please insert another number"))

        if choose == 1:
            answer = num1 + num2
            print(answer)
        if choose == 2:
            answer = num1 - num2
            print(answer)
        if choose == 3:
            answer = num1 * num2
            print(answer)
        if choose == 4:
            answer = num1 / num2
            print(answer)



