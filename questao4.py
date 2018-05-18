consoantes = "BCDFGHJKLMNPQRSTVWXYZ"
vogais = "AEIOU"
cont = 0


for k in range(len(consoantes)):
    for j in range(len(vogais)):
        silaba1 = consoantes[k] + vogais[j]
        for a in range(len(consoantes)):
            for b in range(len(vogais)):
                silaba2 = consoantes[a] + vogais[b]
                for c in range(len(consoantes)):
                    for d in range(len(vogais)):
                        silaba3 = consoantes[c] + vogais[d]
                        if silaba1 != silaba2 and silaba2 != silaba3 and silaba1 != silaba3:
                            print(silaba1 + silaba2 + silaba3)
                            cont += 1

print(str(cont) + " palavras")