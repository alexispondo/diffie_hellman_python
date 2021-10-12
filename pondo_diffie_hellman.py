from math import sqrt
from random import *

def diviseurs(n):
    D,racine=[1],int(sqrt(n))
    fin=racine+1
    for d in range(2,fin):
        if n%d==0 :
            D.extend([d,n//d])
    D=sorted(set(D))
    return D

def puissance(x, k, n): # x^k mod(n)
    puiss = 1
    if k > 0:
        while (k>0):
            if k%2 != 0:
                puiss = (puiss*x)%n
            x =  x*x % n
            k = k // 2
    elif k < 0:
        while (k<=0):
            if k%2 != 0:
                puiss = (puiss*x)%n
            x =  x*x % n
            k = k // 2
    return (puiss)

def est_premier(n):
    D = diviseurs(n)
    D.append(n)
    if len(D) == 2:
        return True
    else:
        return False

def gen_premier():
    print("# Choisr une longueur pour le nombre")
    taille = int(input("$ "))
    deb = "1"
    for i in range(1,taille):
        deb = deb+str(0)
    liste = list(range(int(deb),int(deb+str(0))))
    liste_premier = []
    for elm in liste:
        if est_premier(elm):
            liste_premier.append(elm)
    grand_premier = choice(liste_premier)
    return grand_premier

def est_dans_liste(elm, liste):
    if elm in liste:
        return True
    return False

def generateur(n):
    gen = []
    for i in range(1,n):
        liste_mod = []
        for j in range(1,n):
            a=puissance(i,j,n)
            if a in liste_mod:
                break
            else:
                liste_mod.append(a)
        if list(range(1,n)) == sorted(liste_mod):
            gen.append(i)
    return gen

def main():
    print("\n\n#########################################################################################")
    print("#","Bienvenue dans l'espace de demonstration de Diffie-Hellman".center(85),"#")
    print("#","Pour les besoins de la demonstrations nous allons utiliser ".center(85),"#") 
    print("#","deux personnages: Bob et Alice".center(85),"#")
    print("#########################################################################################")
    q = "non"
    while q == "non":
        print("\n#####################################")
        print("#","Veuillez faire un choix".center(33),"#")
        print("# --------------------------------- #")
        print("# 1- debuter la demo".ljust(35),"#")
        print("# 2- ...".ljust(35),"#")
        print("# 3- Quitter".ljust(35),"#")
        print("#####################################")

        choix = str(input("$ "))

        if choix == "1":
            reprend = "oui"
            while reprend == "oui":
                print("\n#####################################")
                print("# Veuillez entrer un nombre premier")
                print("#")
                print("# Voulez vous generer le nombre premier ?")
                print("# O- Oui")
                print("# (Other key)- Non")
                rep = input("$ ")
                if rep.upper() == "O":
                    nbr_premier = gen_premier()
                    print("# Le nombre premier generer est:", nbr_premier)
                else:
                    print("# Entrer manuelement le nombre:")
                    nbr_premier = int(input("$ "))
                if est_premier(nbr_premier):
                    print("\n#####################################")
                    print("# liste de generateurs de {}".format(nbr_premier).ljust(35),"#")
                    list_gen = generateur(nbr_premier)
                    print("#",list_gen)
                    reprend = "oui"
                    while reprend == "oui":
                        print("# Choisir un generateur")
                        g = int(input("$ "))
                        if est_dans_liste(g, list_gen) == True:
                            print("\n#####################################")
                            print("#","RESUME".center(33),"#")
                            print("# --------------------------------- #")
                            print("# p = {}".format(nbr_premier).ljust(35),"#")
                            print("# g = {}".format(g).ljust(35),"#")
                            print("#####################################")

                            print("\n#####################################")
                            print("# Entrer le secret de bob")
                            b = int(input("# b= "))

                            print("# Entrer le secret de Alice")
                            a = int(input("# a= "))

                            B = puissance(g,b,nbr_premier)
                            A = puissance(g,a,nbr_premier)                            
                            print("\n#############################################################################")
                            print("#","Detail".center(73),"#")
                            print("# ------------------------------------------------------------------------- #")
                            print("# Espace BOB".ljust(37),"# Espace ALICE".ljust(37),"#")
                            print("# BOB calcul B=g^b mod(p)".ljust(37),"# Alice calcul A=g^a mod(p)".ljust(37),"#")
                            print("# B = {}".format(B).ljust(37),"# A = {}".format(A).ljust(37),"#")
                            print("#","Echange des valeures obtenues".center(73),"#")
                            print("#","A<====>B".center(73),"#")
                            print("# BOB calcul maintenant A^b mod(p)".ljust(37),"# ALICE calcul maintenant B^a mod(p)".ljust(37),"#")
                            print("# A^b = g^(a*b) mod(p) = {}".format(puissance(g,a*b,nbr_premier)).ljust(37),"# B^a = g^(b*a) mod(p) = {}".format(puissance(g,b*a,nbr_premier)).ljust(37),"#")
                            print("#############################################################################")
                            print("\nOn a bien demontré Diffie-Hellman car g^(a*b) = g^(b*a)")
                            q = "non"
                            break
                        else:
                            print("\nveuillez selectionner un élement de la liste\n")
                            print(list_gen)
                    print("Voulez-vous reprendre ?")
                    break                    
                else:
                    print("Le nombre entré n'est pas premier")
                    reprend = "oui"
        elif choix=="3":
            q="oui"

main()