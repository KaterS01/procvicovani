#BMI = (weight v kg) / (height v m)na 2

height = float(input("Zadejte svou výšku v metrech:\n"))
weight = float(input("Zadejte svou váhu v kg:\n"))
bmi = weight / height**2
bmi = round(bmi, 1) 


if bmi <= 18.5:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte podváhu")
elif 18.5 < bmi <= 24.9:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte normální váhu")
elif 24.9 < bmi <= 29.9:
     print(f"Váš BMI má hodnotu {round(bmi,1)}, máte nadváhu")
elif 29.9 < bmi <= 34.9:
     print(f"Váš BMI má hodnotu {round(bmi,1)}, máte obezitu 1.stupně")
else:
    print(f"Váš BMI má hodnotu {round(bmi,1)}, máte extrémní obezitu")

