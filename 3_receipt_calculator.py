#Gör ett program som upprepade gånger ber användaren skriva in ett tal.
print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
receipt_sum  = 0.0
while (1):
    receipt = input("Skriv in ett belopp: ")
    if receipt == "quit":
        print(f"Det blir {receipt_sum} kr totalt. Välkommen åter!")
        break
    else:
        receipt_sum += float(receipt)

#3.2 programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
no_of_guests = int(input("Hur många är ni? "))

#3.3  programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.
tip = input("Hur många procents dricks tänker ni ge? (ange som heltal) ")
if tip == "":
    print("Antar att du vill ge 10% i dricks")
    tip = 10
receipt_sum = receipt_sum * int(tip) / 100 + receipt_sum
cheque_per_person = receipt_sum / no_of_guests
print(f"Det blir {receipt_sum} kr totalt, alltså {cheque_per_person} kr per person. Välkommen åter!")


