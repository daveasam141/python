import random
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
response=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if response == "0":
    print(rock)
elif response == "1":
    print(paper)
elif response == "2":
    print(scissors)
else:
    print("Invalid Choice")
comp_response=random.choice([rock, paper, scissors])
print(f"Computer chose:\n{comp_response}")
if response == "0" and comp_response == paper:
    print("You lose!")
if response == "0" and comp_response == scissors:
        print("You win!")
if response == "0" and comp_response == rock:
    print("It's a draw!!")
if response == "1" and comp_response == rock:
    print("You win!")
if response == "1" and comp_response == scissors:
    print("You lose!")
if response == "1" and comp_response == paper:
    print("It's a draw!")
if response == "2" and comp_response == rock:
    print("You lose!")
if response == "2" and comp_response == scissors:
    print("It's a draw!")
if response == "2" and comp_response == paper:
    print("You win!")