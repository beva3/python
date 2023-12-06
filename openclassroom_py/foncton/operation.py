#MES fonction :

#somme de deux nombre
def sum(a,b):
    return a+b

#les 7 jours de la semaine
def jour_semaine(index_jour):
    semaine = ["Alahady","Alatsinainy","Talata","Alarobia","Lakamisy","Zoma","Sabotsy"]
    return semaine[index_jour-1]


print(sum(7,8))
print(jour_semaine(0))