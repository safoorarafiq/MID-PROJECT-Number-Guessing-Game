    import random

guess_taken=0



print('welcome to number guessing game :)')
print("Hello! what's your name" )
player_name=input( )
number=random.randint( 1,100 )
print('well,' + player_name + ' i am thinking of number between 1 and 100' )
print('you will have to guess my number in 10 attempts')

while guess_taken < 10:
    remaining_attempts=10-guess_taken
    remaining_attempts=str(remaining_attempts)
    print('you have ' +remaining_attempts+' remaining attempts' )
    print('take a guess')
    guess=int(input( ))
    guess_taken= guess_taken +1
    
    if guess < number :
        print('your guess is too low')   
    elif guess > number :
        print('your guess is too high')
    else :
     guess_taken=str(guess_taken)
     print('good job, ' + player_name + ' you guess my number in,' + guess_taken + ' guesses')
     break

if guess!=number:
    number =str(number)
    print('nope! the number i was thinking of was ' + number )  


