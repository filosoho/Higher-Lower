from art import logo, vs
from game_data import data
from random import randint


def shuffle():
  """Get data from random account"""
  shuffle = randint(0, len(data) - 1) 
  start = data[shuffle]
  return start


def info(account):
  """Format account into printable format: name, description and country"""
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name}, a {description}, from {country}."


def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns 'A' or 'B' if they got it right, 
  false if they got it wrong or 'Error' if 
  the input was incorrect'.
  """ 
  if guess == 'A' or guess == 'B':
    if a_followers > b_followers:
      return "A"
    elif a_followers < b_followers:
      return "B"
  else:
    return "Error"


def play_game():
  print(logo)
  score = 0
  account_a = shuffle()
  account_b = shuffle()

  keep_playing = True
  while keep_playing == True:
    account_a = account_b
    account_b = shuffle()

    while account_a == account_b:
      account_b = shuffle()
  
    print(f"Compare A: {info(account_a)}")
    print(vs)
    print(f"Against B: {info(account_b)}.")

    keep_guessing = True
    while keep_guessing == True:
      guess = input("Who has more followers? Type 'A' or 'B': ").upper()
      a_follower_count = account_a["follower_count"]
      b_follower_count = account_b["follower_count"]
      is_correct = check_answer(guess, a_follower_count, b_follower_count)
      
      print(logo)
      if guess == is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        keep_guessing = False
      elif is_correct == "Error":
        print("Incorrect input. Try again.")
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_guessing = False
        keep_playing = False


play_game()