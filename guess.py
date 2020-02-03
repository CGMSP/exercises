#This was written in python 2.7, so will not run in python 3 or later.
import random #Import randon math feature for later use
comp_num=random.randint(1, 100) #Set variable comp_num as a random number between 1 and 100
prompt='What is your guess? Between 1 and 100. ' #Set variable prompt as string "What is your guess? Between 1 and 100."
num_guesses=0 #Set variable num_guesses to 0
while True: #Loop the following code continuosly 
  person_guess=raw_input(prompt) #Set variable person_guess as the number entered by user when prompted for a guess.
  if (comp_num==int(person_guess)): #If the computer's number is equivalent to the person's guess:
    num_guesses=num_guesses+1 #Add 1 to the variable num_guesses
    print "You're Correct!" #say "You're Correct!"
    print 'Number of guesses: ', # Print out the number of guesses
    print num_guesses
    break #Break the loop
  elif (comp_num>int(person_guess)): # If person's guess was to low,
    print 'Too low!' #Print too low
    num_guesses=num_guesses+1 #Add 1 to the variable num_guesses
  else: #Otherwise
    print 'Too High!' #Print too high
    num_guesses=num_guesses+1 #Add 1 to the variable num_guesses
  if (num_guesses==5): #If player has guessed 5 times,
    print 'game over'#Print game over
    print ' '
    print 'The correct number was ', #Print the correct number
    print comp_num 
    print 'Nice try!'#Print Nice Try
break #Break the loop.
