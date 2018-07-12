print('Hey welcome to this super silly game!')
print('The rules are simple: \n'+
    '1. You pick a number from 1 to 100\n'+
    '2. The snake will also randomly pick a number\n'+
    '3. You can keep playing until your number matches the snake number\n')

guess = [0]
difference = [0]

from random import randint
pynumber = randint(1,100)
    
while True:
    num = input('please choose a number ')
    num = int(num)
   
    if num > 0 and num < 101:
        guess.append(num)
        #print('Snake number is: ',pynumber)
        
        diff = abs(pynumber - num)
        difference.append(diff)

        if diff == 0:
            turn = len(guess)-1
            print('Well done!!!\n')
            print(f'You took {turn} turns to win \n')
            break
        else:
            if len(guess) == 2:
                if diff <= 10:
                    print('WARM\n')
                else:
                    print ('COLD\n')
            else:
                if difference[-1] < difference[-2]:
                    print('WARMER\n')
                else:
                    print('COLDER\n')
    
    else:
        print('Please choose a number within 1 to 100!!!\n\n')
        