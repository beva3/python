
isa = {
    1:"ray",
    2:"roa",
    3:"telo",
    4:"efatra",
    5:"dimy",
    6:"enina",
    7:"fito",
    8:"valo",
    9:"sivy"
}

ampolo = {
    1:"folo",
    2:"roapolo",
    3:"telopolo",
    4:"efapolo",
    5:"dimapolo",
    6:"enimpolo",
    7:"fitopolo",
    8:"valpolo",
    9:"sivifolo"
}
anjato = {
    1:"zato",
    2:"roanjato",
    3:"telonjato",
    4:"efajato",
    5:"dimanjato",
    6:"eninjato",
    7:"fitonjato",
    8:"valonjato",
    9:"sivinjato"
}

def manisa_malagasi(n):
    if n < 10:
        isa_malagasy = isa[n]
        return isa_malagasy
    elif n >=10 and n <100:
        if n%10 == 0:
            isa_malagasy = ampolo[n/10]
            return isa_malagasy
        if n % 10 == 1:
            isa_malagasy = "iraika " + "ambin'ny " + ampolo[(int)(n/10)]
            return isa_malagasy
        else:
            isa_malagasy = isa[n%10] + " ambin'ny " + ampolo[(int)(n/10)]
            return isa_malagasy
    elif n >= 100 and n < 1000:
        if n%100 == 0:
            isa_malagasy = anjato[n/100]
            return isa_malagasy
        else:
            if n%100 == 1:
                tete = "iraika"
            else:
                tete = manisa_malagasi(n%100)
                
            if n-n%100 == 100: isa_malagasy = tete + " amby zato"
            else : isa_malagasy = tete + " sy " + anjato[(int)(n/100)]
            return isa_malagasy

    elif n >= 1000 and n<10000:
        if n % 1000 == 0:
            if n/1000 == 1: isa_malagasy = "arivo"
            else : isa_malagasy = isa[n/1000] + " arivo "
            return isa_malagasy
        else:
            return manisa_malagasi(n%1000) + " sy " + manisa_malagasi(n - n%1000) 
    elif n >= 10000 and n <100000:
        if n % 10000 == 0:
            tete = "iray" if n/10000 == 1 else manisa_malagasi(n/10000)
            return tete + " alina "
        else:
            return manisa_malagasi(n%10000) + " sy " + manisa_malagasi(n - n%10000)
    else: return None
    
for i in range(1,100000):
    print(f" {i} {manisa_malagasi(i)}")
#print(manisa_malagasi(10000))
