def calculator():
    while True:
        calculator = (input('add operator to do your calculation: (+),(-), (*), (**),(/), (//), exit:'))
        if calculator == exit:
            break
        num1 = int(input('enter first number:'))
        if num1 == exit:
            break
        num2 = int(input('enter second number:'))
        if num2 == exit:
            break
        #addition
        if calculator =='+':
            print('[] + []='.format(num1, num2))
            print(num1 + num2)
            #multiplication
        elif calculator == '*':
            print('[] * [] ='.format(num1 * num2))
            print(num1 * num2)
            #substraction
        elif calculator == '-':
            print('[] - [] ='.format(num1, num2))
            print(num1 - num2)
            #division
        elif calculator == '/':
            print('[] / [] = '.format(num1, num2))
            print(num1 / num2)
            #exponatiate
        elif calculator == '**':
            print('[] ** [] = '.format(num1. num2))
            print(num1**num2)
            #modulus
        elif calculator == '//':
            print('[] //[] ='.format(num1,num2))
        else:
            print('run the program')
calculator()

   
