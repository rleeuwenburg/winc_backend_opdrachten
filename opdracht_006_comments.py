kaas = 3      #de prijs van kaas in euro's is 3
melk = 1      #de prijs van melk in euro's is 1
biefstuk = 6  #de prijs van biefstuk in euro's is 6

som = (kaas + melk + biefstuk)
print(som)
# de som is de totaalprijs van 1 item van ieder artikel

gemiddelde = round((som / 3), 2)
print(gemiddelde)
# het gemiddelde is de de gemiddelde prijs van 1 item van ieder artikel

aantalKaas = 2
aantalMelk = 5
aantalBiefstuk = 4

totaal = aantalKaas * kaas + aantalMelk * melk + aantalBiefstuk * biefstuk
print(totaal)

# ------------------------------------------------------------------------------------------
# Geen korting vandaag
# ------------------------------------------------------------------------------------------

"""
kortingPercentage = 15
totaalNaKorting = round(totaal * ((100-kortingPercentage) / 100), 2)
print(totaalNaKorting)
"""
