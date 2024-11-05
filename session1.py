
# === FUNCTIONS ===
# def greeting():
#   return 'hello everyone!'

# === VARIABLES ===
# player_choice="rock"
# get_return_val=greeting()

# === PRINT ===
# print(get_return_val)

# === DICTIONARIES ===
# dict ={"name":"jane", "age" : 7}
# print(dict,'here is dict')

# === LISTS ===
# food=['pizza', 'carrot','tomato']

# === RANDOM LIBRARY USECASE
# import random
# print(random.choice(food));

# a = 30
# b=5

# def find_greater_val(a,b):
# === IF CONDITION ====
#   if a > b :
# === F-STRING ===
#     print(f'{a} is greater than {b}')
#   elif a==b:
#     print(f'{a} is equal to {b}')
#   else:
#     print(f'{a} is less than {b}')

# print(find_greater_val(a,b))

# === WHILE LOOP ===
# i=1
# while i<=5:
#   print(i)
#   i+=1

# === FOR LOOP ===
# for i in range(1,6):

import random
def check_win(player, computer):
  print(f"you chose: {player} , and the computer chose: {computer}")
  if player == computer:
    return "it's a tie"
  elif (player == "rock"):
    if( computer == "scissors"):
       return "rock smashes scissors, you win!"
    else:
        return "paper covers rock, you loose"
  elif (player == "paper"):
      if(computer == "rock"):
        return "paper covers rock, you loose"
      else:
        return "sissors cuts paper, you loose"
  elif (player == "scissors"):  
      if(computer == "rock"):
        return "rock smashes scissors, you loose"
      else:
        return "sissors cuts paper, you win!"


def get_choices():
  options = ['rock', 'paper', 'sissors']
  player_choice = input('Enter a choice (rock,paper,sissors):')
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return check_win(choices['player'], choices['computer'])

result=get_choices()

print(result)