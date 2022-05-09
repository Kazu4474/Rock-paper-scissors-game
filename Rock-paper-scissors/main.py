rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice=[rock, paper, scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# this is because if the user tries to input a number beyond the limit 
if user_choice>=3 or user_choice<0:
  print("invalid number")
else:
  users_move=choice[user_choice]
  print(users_move)
  # computer_choice=random.randint(0,3)
  # computer_move=choice[computer_choice-1]
  # we can also use the above block of code to the same thing just another method
  computer_choice=random.randint(0,2)
  computer_move=choice[computer_choice]
  print("computer choice:")
  print(computer_move)
  # in here i used the variable it self to compare both of them because the numbers and index numbers were not wroking 
  if users_move==rock and computer_move==scissors:
      print("you win")
  elif users_move==scissors and computer_move==rock:
      print("you lose")
  elif users_move==computer_move:
      print("Draw")
  elif users_move>computer_move:
      print("you win")
  elif users_move<computer_move:
      print("you lose")

