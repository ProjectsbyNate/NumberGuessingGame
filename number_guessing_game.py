import random 
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
guess = int(input("Enter your guess: "))
if guess == secret_number:
  print("Congratulations! You guessed the correct number!")
elif guess < secret_number:
  print("Your guess is too low!")
else: 
  print("Your number is too high!")
