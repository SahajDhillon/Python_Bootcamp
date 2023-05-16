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

# Write your code below this line 👇

user_choice = int(input("Enter your choice 0 - rock, 1 - paper, 2 - scissors"))
game_images = [rock, paper, scissors]
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 0 and computer_choice == 1:
    print("You Loose!")
elif user_choice == computer_choice:
    print("You Tied")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("You Loose!")
elif user_choice == 2 and computer_choice == 0:
    print("You Loose!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice < 0 or user_choice >= 3:
    print("Invalid input")
else:
    print("Invalid Value try again")
