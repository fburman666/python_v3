print("** Todo list extravaganza **")
print("1. Se innehållet i to-do-listan")
print("2. Lägga till nya punkter i din lista")
print("3. Markera som klar")
print("4. Se innehållet i färdiglistan")
print("5. Flytta tillbaks från färdiglista till to-do-listan")
print("6. Avbryta programmet")
to_do_list = []
done_list = []

while 1:
    user_input = int(input("Välj ett alternativ: "))
    #Se innehållet i to-do-listan
    if user_input == 1:
        if to_do_list == []:
            print("Din lista är tom")
        else:
            #print(list)
            for element in to_do_list:
                print(" + ", element)

    #Lägga till nya punkter i din lista
    elif user_input == 2:
        element = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        to_do_list.append(element)
        print(f"Ok, lade till {element} i listan.")

    #Markera som klar
    elif user_input == 3:
        element = input("Skriv in vad du vill ta bort ur to-do-listan: ")
        if to_do_list.count(element) >= 1:
            print("Elementet hittat! Vi tar bort det")
            to_do_list.remove(element)
            done_list.append(element)
        else:
            print("Elementet hittades inte tyvärr")

    #Se innehållet i done-listan
    elif user_input == 4:
        if done_list == []:
            print("Färdig-listan är tom")
        else:
            #print(list)
            for element in done_list:
                print(" + ", element)

        # Flytta tillbaks från färdiglista till to-do-listan
    elif user_input == 5:
        element = input("Skriv in vad du vill flytta från färdiglistan till to-do-listan: ")
        if done_list.count(element) >= 1:
            print("Elementet hittat! Vi tar bort det")
            done_list.remove(element)
            to_do_list.append(element)
        else:
            print("Elementet hittades inte tyvärr inte i färdiglistan")

    # Avbryta programmet
    else:
        break
