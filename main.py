import random
guesses = 0
while guesses < 3:
  number = int(random.random()*10)
  user_guess = int(input("Enter a number 0 through 10 "))
  if user_guess == number:
    print("You Win!!")
    break
  else:
    guesses += 1
if guesses == 3:
  print("You Lose")
