# Nederlands Elftal 1988
# Finale EK vs Rusland

hans = "Hans van Breukelen"
berry = "Berry van Aerle"
frank = "Frank Rijkaard"
ronald = "Ronald Koeman"
adri = "Adri van Tiggelen"
gerald = "Gerald Vanenburg"
arnold = "Arnold Mühren"
jan = "Jan Wouters"
erwin = "Erwin Koeman"
marco = "Marco van Basten"
ruud = "Ruud Gullit"
joop = "Joop Hiele"
wilbert = "Wilbert Suvrijn"
john = "John van 't Schip"
johnb = "John Bosman"
wim = "Wim Kieft"
coach = "Rinus Michels"

scoreNL1 = 35 # oranje scoort 1-0 in 35e minuut
scoreNL2 = 54 # oranje scoort 2-0 in 54e minuut

doelpuntenmakers = ('doelpunten gemaakt door: '+ ruud + ', ' + marco)
print (doelpuntenmakers)

print(f'{ruud} scoorde in de {scoreNL1}e minuut.\n{marco} scoorde in de {scoreNL2}e minuut')

voornaam = hans[0:hans.find(' ')]
print(voornaam)

achternaam = hans[(hans.find(' ')+1):len(hans)]
print(achternaam)

print(hans[(hans.find(' ')+1):len(hans)]+", "+hans[0:hans.find(' ')])
print(wim[(wim.find(' ')+1):len(wim)]+", "+wim[0:wim.find(' ')])

print(hans[0]+'. '+hans[(hans.find(' ')+1):len(hans)])
print((len(hans[0:hans.find(' ')])*(hans[0:hans.find(' ')]+'! ')).rstrip())
print((len(hans[0:hans.find(' ')])*(hans[0:hans.find(' ')]+'! ')).rstrip()[-1]==' ')
