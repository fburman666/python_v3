# Slumpa ett hemligt tal
import random
secret = random.randint(1, 100)
iteration = 0
print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")
while 1:
    try:
        guess = int(input("Gissa: "))
        iteration += 1
        if secret == guess:
            print(f"Det är rätt!! Du gjorde det på {iteration} gissningar.")
            break
        elif secret > guess:
            print("Nej, det är för lågt!")
        else:
            print("Nej, det är för högt!")

        if abs(secret - guess) <= 5:
            print(f"Nu börjar det brännas!")

    except ValueError:
        print("Ange ett heltal!")