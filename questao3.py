consoantes = "BCDFGHJKLMNPQRSTVWXYZ"
vogais = "AEIOU"
cont = 0

for k in range(len(consoantes)):
    for j in range(len(vogais)):
        for a in range(len(consoantes)):
            for b in range(len(vogais)):
                print(consoantes[k]+ vogais[j] + consoantes[a] + consoantes[b])
                cont += 1


print(str(cont) + " palavras")

