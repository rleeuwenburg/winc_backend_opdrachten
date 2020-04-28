preiPrijs = int(2)
preiPrijsString = "Prei kost " + str(preiPrijs) + " euro per kilo."
print(preiPrijsString)

preiBestelling = "prei 4"
preiAantal = int(preiBestelling[preiBestelling.find(' '):])
print(preiAantal)

preiTotaalPrijs = preiAantal * preiPrijs
print(preiTotaalPrijs)

broccoliPrijs = float(2.34)
broccoliBestelling = "broccoli 1.6"
broccoliAantal = float(broccoliBestelling[broccoliBestelling.find(' '):])
broccoliTotaalPrijs = round(broccoliAantal * broccoliPrijs, 2)
broccoliString = str(broccoliAantal) + " kilo broccoli kost " + str(broccoliTotaalPrijs) + " euro."
print(broccoliString)

