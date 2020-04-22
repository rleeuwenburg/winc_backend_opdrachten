kaas = 3
melk = 1
biefstuk = 6

som = (kaas + melk + biefstuk)
print(som)

gemiddelde = round((som / 3), 2)
print(gemiddelde)

aantalKaas = 2
aantalMelk = 5
aantalBiefstuk = 4

totaal = aantalKaas * kaas + aantalMelk * melk + aantalBiefstuk * biefstuk
print(totaal)

kortingPercentage = 15
totaalNaKorting = round(totaal * ((100-kortingPercentage) / 100), 2)
print(totaalNaKorting)
