def addition(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2



operation={
    '+':addition,
    '-':subtract,
    '*':multiply,
    '/':division
}



def calculate():
    num1=int(input('Enter your first number: '))
    for operators in operation:
        print(operators)

    game_on=True
    while game_on:

        symbol=input('Choose an option: ')

        if symbol in operation:
            num2=int(input('Enter your second number: '))
            working=operation[symbol]
            calculation=working(n1=num1,n2=num2)
            answer=f'{num1} {symbol} {num2} = {calculation}'
            print(answer)

            ask=input('type "y" if you want to continue with answer or type "p" to start again or type "n" to exit: ').lower()

            if ask =='y':
                num1=calculation
                game_on=True

            elif ask =='p':
                game_on=False
                calculate()


            elif ask=='n':
                game_on=False

        


            
        else:
            print('invalid operator')
            game_on=True


calculate()