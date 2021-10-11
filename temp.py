A = input("entrez un nombre entier: ")
try:
    A = int(A)
except:
    A=input("\n Erreur !!! Veuillez entrer un nombre entier: ")
    A=int(A)
B=input("entrez un deuxieme nombre entier: ")
try:
    B = int(B)
except:
    B = input("\n Erreur !!!, Votre nombre doit etre un nombre entier: ")
    B = int(B)
C = A + B
print("le resultat de ",A," + ",B," = ",C)