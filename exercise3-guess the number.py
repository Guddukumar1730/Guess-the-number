s=18 #selcted number
n=1   #number of guesses
print('*number of gueeses is limited to 10 only')
while(n<=10):
    print('*(hint:number is factor of 578) ')
    g=int(input('GUESS THE NUMBER\n'))
    #guess number
    if g<18:
        print('you have entered wrong number, please enter greater number    ', '  number of guesses left', 10-n)
    elif g>18:
        print('you have entered wrong number, please enter smalller number    ', 'number of guesses left', 10-n)
    else:
        print('YOU WON!\n  ''RESPECT         ' ,'your number of guesses  ' , n)
    n=n+1
    if n>10:
        print('GAME OVER  ', 'BETTER LUCK NEXT TIME')



