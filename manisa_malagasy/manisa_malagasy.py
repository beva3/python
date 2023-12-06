

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
    4:"efatrapolo",
    5:"dimapolo",
    6:"enimpolo",
    7:"fitopolo",
    8:"valpolo",
    9:"sivifolo"
}

def manisa_malagasi(n):

    if n < 10:
        isa_malagasy = isa[n]
        return isa_malagasy
    elif n >10 and n <100:
        if n % 10 == 1:
            isa_malagasy = "iraika " + "ambin'ny " + ampolo[(int)(n/10)]
            return isa_malagasy
        else:
            isa_malagasy = isa[n%10] + " ambin'ny " + ampolo[(int)(n/10)]
            return isa_malagasy
    else: return None
    
    
    
print(manisa_malagasi(99))