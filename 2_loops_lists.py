#1a Skriv färdigt kodexemplet.
answer = 0
for i in range(1,11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55


#1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)
answer = 0
for i in range(1,101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))

#1c Skriv om 1b så att den använder en while-loop.
answer = 0
i = 0
while i < 101:
    answer += i
    i += 1
print("Summan av talen 1 till 100 är: " + str(answer))



#2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
list =  [1, -2, 3, -2, 4, -3]
sum_of_elements = 0
for element in list:
    sum_of_elements += element
print("Summan av alla element i listan blir: ", sum_of_elements)


#3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
movie_list = ["Rocky1", "Rocky2", "Rocky3", "Rocky4"]
print(movie_list)

#3b Lägg till "Fellowship of the ring" sist i listan.
movie_list.append("Fellowship of the ring")
print(movie_list)

#3c Lägg till "The two towers" på första platsen i listan. (index noll)
movie_list.insert(0,"The two towers")
print(movie_list)

#3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
print("Fellowship of the ring har index", movie_list.index("Fellowship of the ring"))

#3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
movie_list.pop(4)
print("Fellowship of the ring har index", movie_list.index("Fellowship of the ring"))

#3f Ta reda på hur lång listan är. (len)
print("Listan har nu längden: ", len(movie_list))

#3g Vänd listan baklänges.
movie_list.reverse()
print(movie_list)

#3h Sortera listan stigande i bokstavsordning.
movie_list.sort()
print(movie_list)