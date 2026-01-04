
print("Vítejte na horské dráze")
heigh = int(input("Jaká je vaše výška v cm?\n"))
bill = 0

if heigh >= 87:
     print("Můžete jet na horské dráze")
     age = int(input("Jaký je váš věk?\n"))
     if age < 12:
         bill = 50
         print("Cena vašeho lístku je 50 Kč")
     elif age < 18:
          bill = 100
          print("Cena vašeho lístku je 100 Kč")
     else:
          bill = 150
          print("Cena vašeho lístku je 150 Kč")
     photo = input("Chcete během jízdy fotku? Ano nebo ne\n")
     if photo.lower()  == "ano":
        bill += 40
        print(f"Vaše cena je {bill} Kč.")

else:
    print("Omlouváme se, ale nemůžete jet na horské dráze")