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
import random

player=int(input("0 for Rock, 1 for Paper & 2 for scissor: "))
cpu = random.randint(0,2)
if player==cpu:
  if player==0:
    print(f"You:{rock}")
    print(f"CPU:{rock}")
  elif player==1:
    print(f"You:{paper}")
    print(f"CPU:{paper}")
  else:
    print(f"You:{scissors}")
    print(f"CPU:{scissors}")
  print("Wow, Its DRAW!")
elif player==0 and cpu==1:
  print(f"You:{rock}")
  print(f"CPU:{paper}")
  print("Well, You Lose")
  print("Better Luck Next Time")
elif player==1 and cpu==2:
  print(f"You:{paper}")
  print(f"CPU:{scissors}")
  print("Well, You Lose")
  print("Better Luck Next Time")
elif player==2 and cpu==0:
  print(f"You:{scissors}")
  print(f"CPU:{rock}")
  print("Well, You Lose")
  print("Better Luck Next Time")
elif player==1 and cpu==0:
  print(f"You:{paper}")
  print(f"CPU:{rock}")
  print("You Won, Wellplayed")
elif player==2 and cpu==1:
  print(f"You:{scissors}")
  print(f"CPU:{paper}")
  print("You Won, Wellplayed")
elif player==0 and cpu==3:
  print(f"You:{rock}")
  print(f"CPU:{scissors}")
  print("You Won, Wellplayed")