import random

print("Welcome to my number guessing game!")
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
    print("Type a number greater than 0 next time.")
    quit()

else:
  print("Type a number next time.")
  quit()

# rand = random.randrange(-1, 11)
rand_num = random.randint(0, top_of_range)
num_of_guesses = 0

while True:
  num_of_guesses += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)

  else:
    print("Type a number next time.")
    continue

  if user_guess == rand_num:
    print("You got it correct!")
    break
  elif user_guess > rand_num:   
      print("You were above the number!")
  else:
      print("You were below the number!")
    
print("You got it in", num_of_guesses, "guesses")


