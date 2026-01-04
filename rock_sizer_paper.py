import random
kámen = 0
papír = 1
nůžky = 2

print("Ahoj, vítej u nové hry.")
user_choice = int(input("Zadej co si vybereš: 0 = kámen, 1 = papír, 2 = nůžky\n"))
if user_choice in [0,1, 2]:
     print("Čekám na protihráče")
else:
     print("Špatná hodnota")

computer_choice = random.randint(0,2)
if computer_choice == 0:
     print("Protihráč si zvolil kámen")
elif computer_choice == 1:
     print("Proithráč si zvolil papír")
elif computer_choice == 2:
     print("Protihráč si zvolil nůžky")
#porovnání
if user_choice == computer_choice:
     print("Remíza")
elif (user_choice == 0 and computer_choice == 2):
      print("Vyhrál jsi! ")
elif (user_choice == 1 and computer_choice == 0):
      print("Vyhrál jsi! ")
elif (user_choice == 2 and computer_choice == 1):
     print("Vyhrál jsi! ")
else:
     print("Počítač vyhrál")