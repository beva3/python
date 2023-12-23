class Rect:
    def __init__(self, longeur, largeur,couleur = "sans color"):
        self.l = longeur
        self.la = largeur
        self.col = couleur


rect = Rect(1,2,"rouge")
print(rect.l)
print(rect.la)
print(rect.col)